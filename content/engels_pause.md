Title: Engels' Pause in China
Author: Chen Zhou
Date: 2015-05-11
Status: draft

<!--
# TODO
* ok 修改文章结构
    * 简略介绍恩格斯停滞文章
    * 先介绍模型，再介绍数据
    * 最后模拟
* ok 查国民收入分布，劳动收入比，资本收入比
* （checked）重新计算储蓄率。Allen (2009) 通过投资 $I$，产出/收入 $Y$ 来回归估计储蓄率，这里我直接用别人估计得储蓄率，可能会对降低估计得到的生产函数的准确性。
* 美化图表，修改图题，坐标，长宽，单位
```{r include=FALSE}
require(ggplot2)
require(pryr)
require(reshape2)
require(stargazer)
```
-->

------------

# 前言 Foreword

本文大体上用中国 1982 至 2009 年的数据再现了 Allen (2009) 在 Engels' Pause 中的研究方法，用迭代调整的方法（不是用回归）求出了中国超越对数生产函数的形式，发现中国的资本对劳动替代弹性长期稳定在 0.88 附近，没有超过 0.9，资本和劳动之间确实不容易替代，但也没有英国 19 世纪初接近于 0 这么极端。同样，我也根据 Solow 模型成功地模拟出了中国的情况，**模型同样适用于中国**，各项指数的模拟值和真实值都十分接近。

根据本文的数据，虽然 1982 至 2009 年中国的资本收入占比的趋势是上升，劳动收入占比的趋势是下降，但是劳动者的实际工资（通过超越对数生产函数求出）并没有停滞，而是一直在增长，虽然增长的速度没有劳动者的人均产出增长的快，所以在这段时间内**恩格斯停滞并没有在中国发生**。

虽然没有得出什么明确的结论或者证明什么观点，但本文还是有几个地方很有意思：

1. 用迭代调整的方法求超越对数生产函数（见 3.3.2），用估计出来的生产函数计算的 GDP 与真实值的**误差大部分小于 0.2 %**。
2. 用 Solow 模型模拟真实经济 （见 3.3），成功模拟出中国 GDP、资本存量、人均产出、实际工资、资本收益率的走势。
3. 还有一点，在求超越对数生产函数的过程中会得到一系列调整过的全要素生产率 $A$，我感觉比赵志耘 (2011) 文章中估计的全要素生产率要靠谱一些，他估计的全要素生产率竟然有负数。
4. 根据超越对数生产函数求出的资本劳动替代弹性，比王灿雄（2014）的估计（0.99~1 之间）更低，而且下降的趋势更明显。

但 Allen 模型的一个缺点在于，它的准确性依赖于不断调整出的全要素生产率 $A$，调整出适合超越对数生产函数的 $A$ 需要真实的数据。因此，这个模型只适用于解释过去的经济现象，用来预测未来的话准确度会大大下降。

```
红色方框中是具体的操作代码，所有代码都是 R 语言，有兴趣的话可以按照代码重新验证一下。
```

# Allen 对恩格斯停滞的解释 Allen's Explanation for Engels' Pause
## 什么是“恩格斯停滞” What's Engels' Pause
恩格斯停滞指的是英国 19 世纪初，工业革命使得技术进步，工人的人均产出不断增加，资本的收益率不断上升，而工人的实际工资发生了停滞。

## 对恩格斯停滞的解释 Explanations for Engels' Pause
除了认为是历史偶然因素造成的外，对恩格斯停滞的解释有很多种：

* 马尔萨斯认为人口的增长过快，只要工人的工资增加，人口就快速增加，使得平均实际工资不变。
* 马克思认为技术的进步带有节约劳动的倾向，技术进步使得对劳动的需求减少了，使得实际工资停滞。
* 无限劳动力供给理论认为农村为城市提供了无限劳动力，只有当农村的剩余劳动力被完全吸纳了，工人的实际工资才会上升。
* Engels' Pause 的作者 Allen 认为是 19 世纪初英国的资本对劳动替代弹性接近于 0 造成的实际工资停滞。

Allen 解释说，英国工业革命兴起，技术进步导致对资本需求的增加，使资本的收益率增加，资本收益率增加也就增加了资本的使用成本，人们需要支付更多的利息去获得资本，如果此时资本与劳动十分容易替代的话，人们可以雇佣更多的劳动替代资本。例如，工厂不必购买更先进机器，有时雇佣更多的劳动力也能达到同样的产量。这样，资本收益率的增加也会导致对劳动需求的增加。而工业革命时的资本主要用于城市化，满足工人在城市生活的基本要求，这时劳动对资本的替代能力是很低的，即替代弹性很低，对资本的需求无法用更多的劳动力满足，资本的收益增加，劳动力的收入相对停滞，工人没有享受到社会进步的成果，恩格斯停滞出现了。

Allen 的核心观点认为，当资本的积累满足了技术进步的要求，城市化完成，整个社会的资本劳动替代弹性主要由工厂内的资本劳动替代弹性体现，劳动力能替代资本，对资本需求的增加导致资本收益增加，进而人们用劳动力替代资本降低成本，劳动力的需求增加，劳动力的收入也能增长，恩格斯停滞自动消失。

## Allen 观点的验证 Prof of Allen's Theory
Allen 构建了一个基于 Solow 模型的模型，生产函数使用了能够反映替代弹性变化的超越对数生产函数，并通过迭代调整的方法求出超越对数生产函数的参数。发现 19 世纪初英国的资本劳动替代弹性接近于 0，然后通过模型模拟真实的经济，成功再现了英国 19 世纪初工人实际工资停滞，19 世纪中后期实际工资增长的现象。因此，仅仅通过要素替代弹性的变化就能解释恩格斯停滞了。

# 对中国的分析 China's Situation

## 数据 Data
要估计出中国超越对数生产函数的参数，必须知道国民生产总值、劳动力、资本存量以及要素收入占比的数据。

### 国民核算 National Accounts
**国民生产总值、劳动力、资本存量**数据直接引用了赵志耘、杨朝峰（2011）的估算。国民收入以2000价格计算的实际GDP为代表，单位为亿元；劳动力为当年就业人数的年中数，单位：万人，来源于统计年鉴；资本存量来自于《中国国内生产总值核算历史资料 (1952—2004)》公布的数据，2004年后的数据为间接估算，当年价格年中数，单位亿元。
```{.r}
# 实际GDP 劳动力 资本存量
colnames <- c("year", "realgdp", "labor", "capitalstock", "a")
data <- read.table("data.txt", col.names=colnames)
dd_sub <- data[, c("year", "realgdp", "capitalstock")]
dd <- melt(dd_sub, id=c("year"))
p <- ggplot(dd)
p + geom_line(aes(x=year, y=value, color=variable)) + 
    scale_color_discrete(labels=c("实际 GDP", "资本存量")) +
    labs(title="实际 GDP 和资本存量（1982-2009）",
         x="年份", y="GDP，资本存量（亿元）") +
    theme(legend.title=element_blank())
```

### 要素收入占比 Factor Shares
中国要素收入占比的数据来源于韩雷（2012），其中，劳动收入有两种处理，一种对个体业主的收入按资本收入占比进行了分劈，另一种将个体业主的收入全部归为劳动收入。这里采用了第二种。这里我们把政府的角色省略，其在要素收入分配中的比例不足 1%。
```{.r}
# 要素收入占比
shares <- read.table("share.txt", header=TRUE)
dd_sub <- shares[, c("year", "l2", "k2")]
dd <- melt(dd_sub, id=c("year"))
p <- ggplot(dd)
p + geom_line(aes(x=year, y=value, color=variable)) +
    scale_color_discrete(labels=c("劳动收入占比", "资本收入占比")) +
    labs(title="中国要素收入占比（1982-2009）",
         x="年份", y="要素占比") +
    theme(legend.title=element_blank())
```

<!--### 储蓄率
**储蓄率**用资本形成率代替，来源于《中国统计年鉴》支出法国内生产总值部分。资本形成率已经考虑了折旧因素，所以在后面的模拟过程中资本折旧项 $\delta K$ 将会省略。
```{r}
# 储蓄率（资本形成率）
colnames <- c("year", "gdp", "consumption", "capital formation", "net exports", "consumption rate", "capital formation rate")
gdpdata <- read.table("capital_formation_rate.txt", col.names=colnames)
plot(x=gdpdata$year, y = gdpdata$capital.formation.rate)
```
-->

### 主要数据 Data Used
```{.r}
data$capital_formation_rate <- gdpdata$capital.formation.rate
data$labor_share <- shares$l2
data$capital_share <- 1 - shares$l2
k <- data$capitalstock
l <- data$labor
alpha <- data$labor_share
beta <- data$capital_share
gdp <- data$realgdp
phi_k <- data$capital_share
phi_l <- data$labor_share
dd <- data
dd$year <- NULL
dd$a <- NULL
dd$capital_formation_rate <- NULL
stargazer(dd, type="text", title="主要数据")
```

实际 GDP、资本存量、和劳动力（就业人数）数据来自于赵志耘（2014），要素收入占比的数据来自于韩雷（2012）
## 模型 Model

我们的目标是用中国的数据重现 Allen 的方法。Allen 主要是要证明不需要其他的干预，随着资本积累，资本的逐渐满足技术进步的要求，资本对劳动的替代弹性逐渐上升，工人的实际工资会逐渐上升，摆脱停滞状态。Allen 通过采用生产函数为超越对数方程形式的 Solow 模型，成功模拟出了工人实际工资先停滞后上升的状况，说明没有其他的干预，经济也会自动使得实际工资上升。

Allen 的研究主要分为两个步骤：

1. 求出模型的各个参数：用迭代调整的方法求出超越对数生产函数的具体形式，用回归的方法求出储蓄方程中的储蓄率
2. 用模型模拟真实的经济：
    * 首先用超越对数生产函数模拟出资本收入占比。
    * 然后用资本收入占比结合储蓄方程就能模拟出每一年的储蓄率
    * 有了储蓄率，再结合全要素生产率和劳动力，Solow 模型就能模拟出接下来一系列的资本存量和国内生产总值。

对中国的分析同样遵循这几个步骤。

### 理论框架 Theory
首先介绍一下 Allen 的模型，对中国的分析也基于这个模型，只是去掉了土地要素。
Allen 文中的模型基于索洛增长模型：
$$
Y = f(AL,K,T)\\
K_t = K_{t-1} + I_t - \delta K_{t-1}\\
I = sY\\
$$
储蓄率是资本资本收入占比和土地要素收入占比的函数：
$$I = (S_K\phi_K + S_T\phi_T)Y$$
工资率、利润率、地租可以由以下公式得到：
$$
w = \phi_L \frac{Y}{L}\\
i = \phi_K \frac{Y}{K}\\
r = \phi_T \frac{Y}{T}\\
$$
生产函数为超越对数生产函数（这里并没有完整给出，后面有完整的中国超越对数生产函数的形式）：
$$\ln{Y} = \alpha_0 + \alpha_K\ln{K}+\alpha_L\ln{AL}...$$

通过迭代调整求出生产函数的参数，这过程中也对应的全要素生产率也能求出来。

生产函数的具体形式求出来以后，就可以根据公式模拟出各要素的收入占比，再根据回归得出的储蓄率的公式，又可以模拟出储蓄率。在后面的模拟过程中只有劳动力 $L$ 和 土地$T$ 是外生的真实值，由于中国的模型中没有土地，所以只有劳动力 $L$ 使用了真实值。

要使这个模型能够模拟出真实的经济，必须求出生产函数与储蓄方程的具体形式，我们首先求储蓄方程，在估计超越对数生产函数。

### 储蓄方程 Saving Equation
在 Allen (2009) 的模型中，估计储蓄率的关系式是
$$I = (S_K\phi_K + S_T\phi_T)Y$$
其中 $S_K$ 是资本的边际储蓄倾向，$K_T$ 是土地的边际储蓄倾向。而在我们的模型中没有考虑土地要素，又由于 $\phi_L$ 和 $\phi_L$ 共线，所以我们储蓄率的关系式为
$$
\frac{I}{Y} = S_K\phi_K
$$
通过回归可以得到参数 $S_K$ 的值。
```{.r}
# 计算储蓄率，用上期的资本存量减去本期的资本存量得到本期的投资额
# 再用本期的投资额除以本期的 GDP 得到本期的储蓄率
saving_rate <- function(k, y) {
    saving_rate_iter <- function(idx, s=NA) {
        s[idx] <- (k[idx+1] - k[idx]) / y[idx]
        if (idx >= length(y)) {
            s
        } else {
            saving_rate_iter(idx+1, s)
        }
    }
    saving_rate_iter(1)
}
# 计算出真实的储蓄率
s <- saving_rate(k=k, y=gdp)

# 对储蓄率关于资本收入占比，劳动收入占比回归
lm_saving_rate <- lm(s ~ phi_k)
lm_saving_rate_outcome <- summary(lm_saving_rate)
stargazer(lm_saving_rate, type="text")
```
从回归结果可以看出储蓄率与资本收入占比的相关性十分显著，资本收入占比越高，储蓄率越高。我们模型中的储蓄方程由此得出
$$
\frac{I}{Y} = 0.82\phi_K - 0.09
$$
通过这个方程我们就可以在后面的模拟中模拟出储蓄率了。

### 超越对数生产函数 Translog Production Function
由于不考虑土地要素，Allen (2009) 中的三要素生产函数要变成两要素超越对数方程。
$$\ln{Y_t} = \beta_0 + \beta_K\ln{K_t} +\beta_L \ln{AL_t}+\frac{1}{2}\beta_{KK}(\ln{K_t})^2 + \frac{1}{2}\beta_{LL}(\ln{AL_t})^2+\beta_{KL}\ln{K_t}\cdot \ln{AL_t}$$

分别对$\ln{K}, \ln{L}$求导可得
$$\frac{d\ln{Y}}{d\ln{K}}=\beta_K + \beta_{KK}\ln{K}+\beta_{KL}\ln{AL}$$
$$\frac{d\ln{Y}}{d\ln{L}}=\beta_L + \beta_{LL}\ln{AL}+\beta_{KL}\ln{K}$$

其中，$\frac{d\ln{Y}}{d\ln{K}} = \frac{K}{Y} = \phi_K$, $\frac{d\ln{Y}}{d\ln{L}}=\frac{L}{Y}=\phi_L$，分别是资本与劳动的收入占比。从而，可以得到
$$\phi_K=\beta_K + \beta_{KK}\ln{K}+\beta_{KL}\ln{AL}$$
$$\phi_L=\beta_L + \beta_{LL}\ln{AL}+\beta_{KL}\ln{K}$$
与 Allen(2009) 一样，带入附加限定条件，$\beta_K + \beta_L = 1$ 即 $\beta_L = 1 - \beta_K$，进一步可以得到$$\phi_K=\beta_K + \beta_{KK}\ln{K}+\beta_{KL}\ln{AL}$$
$$\phi_L - 1=-\beta_K + \beta_{LL}\ln{AL}+\beta_{KL}\ln{K}$$
写成矩阵形式
$$\left|\begin{array}{c}
\phi_K \\
\phi_L - 1
\end{array}\right|
=
\left|\begin{array}{cccc}
1 & \ln{K} & \ln{AL} & 0 \\
-1 & 0 & \ln{K} & \ln{AL} 
\end{array}\right|
\left|\begin{array}{c}
\beta_K \\
\beta_{KK} \\
\beta_{KL} \\
\beta_{LL} 
\end{array}\right|
$$
这里有两个方程，两个点就能求出右边四个未知参数。$phi_K, phi_L, K, L$ 我们都有数据，带入两个点的数据我们就能求出四个未知数。

### 迭代调整 Calibration
除了四个未知参数外，我们没有全要素生产率 $A$ 的数据，为了求出四个未知参数，
必须先估计$A$的大小，我们还是采用 Allen(2009) 的方法。注意，这里估计 $A$
的值，目的不在于找出一个能真实反映中国技术进步的指数，我们只是需要一个 $A$
使得我们的超越对数生产函数尽可能的与真实值符合，
使得从超越对数生产函数得出的资本劳动替代弹性反映现实。

1. 选取 1985 和 2005 年的数据计算未知参数，确定在 1985 年$\phi_K = 0.40, \phi_L = 0.60$
$K=45950.04,L=49035.0$，
在 2005 年$\phi_K = 0.47, \phi_L = 0.53, K=396083.98,L=75512.5$。
2. 通过柯布道格拉斯生产函数算出每一年的 $A$，
计算中，假设 $A$ 在 1982 年为 1。具体计算函数见代码中的 `A_from_Cobb_Dougla` 函数。
3. 1985 和 2005 年的 $A$ 带入进上面的方程组（矩阵）中，未知参数就能计算出来了（代码见 `coef_e`）。
这些参数不会符合现实，这些参数计算出来的 GDP 和真实值相差很大，因为 $A$ 是从另一个方程中算出来的。 
4. 修改每一年 $A$ ，使得通过超越对数生产方程计算出来的 GDP 与真实数据相等。这里不能通过解方程求 $A$，很多情况是无解的。我这里用二分法一个一个值试探，找到一个使得GDP 估计值最接近 GDP 真实值的 $A$。这里具体的代码见 `A_calibration` 函数。
5. 用上一步计算出来的 1985、2005 年的 $A$，重新计算四个未知参数。
6. 回到第四步，直到估计出来的 GDP 与真实 GDP 几乎相等。第 4 步和第 5 步不断循环，我们参数的估计会更加精确。控制整个循环的函数为 `calibration`。

<!--在迭代之前我们必须要把 Cobb-Doublags 和超越对数生产函数的常数项求出来。令 1985 起始年的 $A$ 为 1 ，就可以分别求出它们的常数项。C-D 函数的常数项为
$$
\ln{A_0} = \alpha \ln{AL} + \beta \ln{K} - \ln{Y}
$$
超越对数生产函数的常数项为
$$
\beta_0 = \ln{Y} - \beta_K \ln{K} - \beta_L\ln{AL}
- \frac{1}{2} \beta_{KK}(\ln{K})^2
- \frac{1}{2} \beta_{LL}(\ln{L})^2
- \beta_{KL}\ln{K}\ln{AL}
$$]-->

运行代码就能得到估计出超越对数生产函数的参数和估计出的 $A$。实际上，**8 次**迭代后，
估计出的参数和 $A$ 就能使得估计出的 GDP 与真实 GDP 之差小于 100。
```{.r}
# Cobb-Douglas 生产函数，a0是常数项的对数形式
cd <- function(a0, A, l, k, alpha, beta) {
    exp(a0) * (A * l) ^ alpha * k ^ beta
}

# 计算 C-D 生产函数的常数项
a0_of_Cobb_Douglas <- function(y, k, l, alpha, beta, A=1) {
    log(y) - alpha * log(A*l) - beta * log(k)
}

# 计算用 C-D 生产函数计算初始 A
A_from_Cobb_Douglas<- function(y, a_0, alpha, beta, k, l) {
    tmp <- log(y) - a_0 - alpha * log(l) - beta * log(k)
    exp((1/alpha) * tmp)
}

# 计算超越对数生产函数常数项
b0_of_translog <- function(coefs, y, k, l, A=1) {
    log(y) - coefs["beta_k"] * log(k) -
    coefs["beta_l"] * log(A*l) -
    1/2 * coefs["beta_kk"] * (log(k))^2 -
    1/2 * coefs["beta_ll"] * (log(A*l))^2 -
    coefs["beta_kl"] * log(k) * log(A*l)
}

# 用 A 得出新的方程组矩阵用来算未知参数
new_matrix_from_A <- function(A, k, l) {
    # 方程组框架
    elements <- c(1, -1, 1, -1,
                  log(k[1]), 0, log(k[2]), 0,
                  log(A[1] * l[1]), log(k[1]), log(A[2] * l[2]), log(k[2]),
                  0, log(A[1] * l[1]), 0, log(A[2] * l[2]))
    matrix(elements, nrow=4, ncol=4)
}

# 求未知参数
coef_e <- function(matrix_from_A, b) {
    # 解方程组 solve(a,b) ax=b
    ret <- solve(matrix_from_A, b)
    ret <- c(1-ret[1], ret)
    names(ret) <- c("beta_l","beta_k", "beta_kk", "beta_kl", "beta_ll")
    ret
}

# 根据参数返回新的生产函数
production_function <- function(coefs, beta_0=0) {
    function(k, l, A) {
        lnY <- beta_0 + coefs["beta_k"] * log(k) + coefs["beta_l"] * log(A * l) + 0.5 * coefs["beta_kk"] * (log(k))^2 + 0.5 * coefs["beta_ll"] * (log(A * l))^2 + coefs["beta_kl"] * log(k) * log(A * l)
        exp(lnY)
    }
}

# 调整 A 使得从超越对数生产函数求出的 GDP 接近真实的 GDP
A_calibration <- function(gdp, coefs, A, k, l, b0, tolerance=100) {
    production_func <- production_function(coefs=coefs, beta_0=b0)
    p_func <- partial(production_func, k=k, l=l)
    A_calibration_iter <- function(A, A_max=100, A_min=0) {
        gdp_e <- p_func(A)
        gap <- gdp_e - gdp
        if (abs(gap) < tolerance || A_max - A_min < 1e-11) {
            A
        } else if (gap > 0) {
            A_candidate <- (A - A_min) * 0.5 + A_min
            A_max <- A
            A_calibration_iter(A_candidate, A_max=A_max, A_min=A_min)
        } else {
            A_candidate <- (A_max - A) * 0.5 + A
            A_min <- A
            A_calibration_iter(A_candidate, A_max=A_max, A_min=A_min)
        }
    }
    A_calibration_iter(A)
}

# 得到一系列调整后的 A
# p_func 为生产函数，用来记算 GDP 估计值
A_lst_calibrated <- function(A_origin, coefs,
                             A_max=10,
                             A_min=0,
                             y, k, l, beta_0,
                             tolerance=100) {
    ret <- c()
    for (i in 1:length(A_origin)) {
        A_calibrated <- A_calibration(coefs=coefs,
                                      A=A_origin[i],
                                      gdp=y[i],
                                      k=k[i],
                                      l=l[i],
                                      b0=beta_0,
                                      tolerance=tolerance)
        ret <- append(ret, A_calibrated)
    }
    ret
}

calibration <- function(A_cd, k, l, alpha, beta, gdp,
                        tolerance=100, points=c(4,24)) {
    # 循环体
    calibration_iter <- function(A, iter=1) {
        # 根据 A 得出新的方程组
        matrix_from_a <- new_matrix_from_A(A=c(A[points[1]], A[points[2]]),
                                           k=c(k[points[1]], k[points[2]]),
                                           l=c(l[points[1]], l[points[2]]))
        # 根据新的方程组 估计未知参数
        coefs <- coef_e(matrix_from_a,
                        b=c(beta[points[1]], alpha[points[1]],
                            beta[points[2]], alpha[points[2]]))
        # 求 beta_0
        b0 <- b0_of_translog(coefs, y=gdp[1],
                             k=k[1], l=l[1],)
        # 根据参数得出新的生产函数，并根据新的生产函数估计 GDP
        production_func <- production_function(coefs, b0)
        gdp_e <- production_func(k=k,l=l,A=A)
        # 如果估计的 GDP 与真实的 GDP 相似
        gap <- abs(gdp_e - gdp)
        if (all(gap < tolerance)){
            coefs <- c(b0, coefs)
            names(coefs) <- c("beta_0", "beta_l", "beta_k",
                              "beta_kk", "beta_kl", "beta_ll")
            list(coefs, A)
        } else {
            A <- A_lst_calibrated(A_origin=A,
                                  coefs=coefs,
                                  y=gdp,
                                  k=k, l=l, beta_0=b0)
            calibration_iter(A, iter=iter+1)
        }
    }
    calibration_iter(A_cd)
}

a0 <- a0_of_Cobb_Douglas(y=gdp,k=k, l=l,
                         alpha=alpha, beta=beta)
A <- A_from_Cobb_Douglas(y=gdp, a_0=a0[1],
                         alpha=alpha, beta=beta,
                         k=k, l=l)
ret <- calibration(A_cd=A, k=k, l=l,
                   alpha=alpha, beta=beta, gdp=gdp,
                   tolerance=100)
```

迭代调整出的超越对数生产函数的参数：
```{.r}
# 参数
coefs <- ret[[1]]
print(coefs)
```

迭代调整出的全要素生产率 $A$：
```{.r}
# 1982-2009估计出的A
A <- ret[[2]]
print(A)
```

现在我们可以得到生产函数的具体形式大概为
$$\ln{Y_t} = -6.08 + 0.77\ln{K_t} +0.22\ln{AL_t}+\frac{1}{2}\cdot 0.05(\ln{K_t})^2 + \frac{1}{2}\cdot 0.21(\ln{AL_t})^2-0.09\ln{K_t}\cdot \ln{AL_t}$$

我们将估计出的全要素生产率 $A$，资本存量 $K$，劳动力 $L$，带入上面超越对数生产函数就能得到估计出的 GDP，我们用估计的 GDP 和真实的 GDP 比较一下，如果他们之间相差很小，那么这个超越对数生产函数的表现就很好。

```{.r}
gdp_e <- production_function(coefs=coefs, beta_0=coefs["beta_0"])(k=k, l=l, A=A)
gap <- gdp - gdp_e
qplot(data$year, gap/gdp*100) + labs(title="超越对数生产函数拟合情况",
                                 x="年份", y="GDP 估计值与真实值相差的比例(%)")

```

从图中可以看到，估计值与真实值的差距大部分不超过 0.2%，超越对数生产函数的表现很好。

### 资本对劳动替代弹性 Elasticity of Subsitution of Capital to Labor
前面已经求出超越对数生产函数的参数，
资本与劳动替代弹性计算公式为
$$
\sigma_{KL} = (1 + \frac{
-\beta_{KL} + \frac{\eta_K}{\eta_L}\beta_{LL}
}{
-\eta_K + \eta_L
})^{-1}
$$
其中，$\eta_K$ 是资本投入的产出弹性，$\eta_L$ 是劳动投入的产出弹性
$$
\eta_K = \beta_K + \beta_{KL}\ln{AL} + \beta_{KK}\ln{K}\\
\eta_L = \beta_L + \beta_{KL}\ln{K} + \beta_{LL}\ln{AL}
$$
由此可以计算中国 1982-2005 资本对劳动的替代弹性。
```{.r}
# 资本对劳动替代弹性
sigma_kl <- function(coefs, A, k, l) {
    beta_0 <- coefs["beta_0"]
    beta_k <- coefs["beta_k"]
    beta_l <- coefs["beta_l"]
    beta_kk <- coefs["beta_kk"]
    beta_kl <- coefs["beta_kl"]
    beta_ll <- coefs["beta_ll"]

    eta_k <- beta_k + beta_kl * log(A*l) + beta_kk * log(k)
    eta_l <- beta_l + beta_kl * log(k) + beta_ll * log(A*l)
    
    up <- -beta_kl + eta_k / eta_l * beta_ll
    base <- -eta_k + eta_l
    (1 + up/base)^(-1)
}

sigma <- sigma_kl(coefs=coefs, A=A, k=k, l=l)
year <- 1982:2009
sigma <- data.frame(year, sigma)
```

根据超越对数生产函数求出的资本劳动替代弹性：
```{.r}
summary(sigma$sigma)
```

从资本对劳动替代弹性的情况来看，1982年至2009年中国资本与劳动不容易相互替代，替代弹性都小于0.9，平均值0.88，而且最小值与最大值相差不大，说明近三十年来中国资本与劳动间的替代能力没有显著变化。而王灿雄（2014）的估计结果是，中国 1978 至 2010 年的资本劳动替代弹性没有超出 $[0.99, 1]$ 的区间，我们这里估计出来的资本劳动替代弹性更低，下降的趋势更明显，

从发展趋势来看，中国的资本对劳动替代率长期处于下降趋势。
```{.r}
p <- ggplot(sigma, aes(year))
p + geom_line(aes(y=sigma)) +
    labs(title="中国资本劳动替代弹性（1982-2009）",
         x="年份", y="资本劳动替代弹性")
```

中国的资本对劳动替代率确实低于 1，资本与劳动之间不容易替代，但和 Allen(2009) 测量出的英国工业革命时接近于 0 的资本对劳动替代率相比，还是很高的。资本劳动替代率对于中国的解释力，恐怕就没有对于英国工业革命时的解释力强了。当然，这 0.2 个单位的替代弹性是不是就足够导致劳动收入的大幅下降呢，还是 0.8 的替代弹性就可以近似看成完全替代呢，这还需要进一步研究。

## 模型的表现 Performance of this Model
接下来要通过模型模拟，看这个估计出的超越对数生产函数是否符合现实。模拟的方法：已知 1982 年的国民生产总值 $Y$ 、资本存量 $K$ 和储蓄率 $s$，根据 Solow 模型的第三个式子
$$I = sY$$
我们可以得出 1983 的投资 $sY$，根据 Solow 模型的第二个式子
$$K_t = K_{t-1} + I_t - \delta K_{t-1}$$ 
进而我们可以知道 1983 年的资本存量 $K + sY$，（由于我们的储蓄率就是资本形成率，资本折旧可以不考虑了）再由前面估计出来的超越对数生产函数
$$\ln{Y_t} = \beta_0 + \beta_K\ln{K_t} +\beta_L \ln{AL_t}+\frac{1}{2}\beta_{KK}(\ln{K_t})^2 + \frac{1}{2}\beta_{LL}(\ln{AL_t})^2+\beta_{KL}\ln{K_t}\cdot \ln{AL_t}$$
我们就可以模拟出 1983 年的国民生产总值了，进而我们又可以模拟出 1984 年的资本存量，1984 年的国民生产总值。用这个方法，我们就可以由一个初始点（1982）通过模型模拟出后面一系列的值。

### 要素收入占比的模拟 Simulation of Factor shares
超越对数生产函数已知，根据前面推导的公式 $\phi_K = \beta_K + \beta_{KK}\ln{K}+ \beta_{KL}\ln{AL}$，使用真实的资本存量 $K$、劳动力 $L$、和调整过的 $A$，我们可以模拟出模型中的资本收入占比了，用 1 减去资本收入占比就得到劳动收入占比了。
```{.r}
# 估计资本收入份额
capital_share <- function(coefs, A, k, l) {
    coefs["beta_k"] + coefs["beta_kk"] * log(k) +
    coefs["beta_kl"] * log(A * l)
}

# 模型中估计得资本收入份额
phi_k_simulated <- capital_share(coefs=coefs, A=A, k=k, l=l)
phi_l_simulated <- 1 - phi_k_simulated
simulation <- data.frame(year, phi_k, phi_k_simulated,
                         phi_l, phi_l_simulated)
dd_sub <- simulation[, c("year", "phi_k", "phi_k_simulated", "phi_l", "phi_l_simulated")]
dd <- melt(dd_sub, id=c("year"))
p <- ggplot(dd)
p + geom_line(aes(x=year, y=value, color=variable)) +
    labs(title="要素收入份额的模拟（1982-2009）",
         x="年份", y="比例") +
    scale_color_discrete(labels=c("资本收入占比真实值",
                                  "资本收入占比模拟值",
                                  "劳动收入占比真实值",
                                  "劳动收入占比模拟值")) +
    theme(legend.title=element_blank())    

```

模拟的要素收入占比很好地模拟出了中国近 20 年来资本收入占比不断上升，劳动收入占比不断下降的情况。

#### GDP与资本存量的模拟 Simulation of GDP and Capital Stock
资本收入占比模拟出来了，根据前面已经得到的储蓄方程 $\frac{I}{Y}=0.82 \phi_K-0.09$，我们可以得到模拟的储蓄率。
```{.r}
# 估计出的储蓄方程
saving_rate_simulation <- function(intercept, coef, phi_k) {
    intercept + coef * phi_k
}

# 估计出的储蓄率
intercept <- coef(lm_saving_rate_outcome)["(Intercept)", "Estimate"]
coef <- coef(lm_saving_rate_outcome)["phi_k", "Estimate"]
s_simulated <- saving_rate_simulation(intercept=intercept,
                                      coef=coef, phi_k=phi_k_simulated)
```

将前面迭代调整出的全要素生产率 $A$ 、模拟出的储蓄率 $s$ 和劳动力 $L$ 带入 Solow 模型，给定初始点，就可以开始模拟出后续年份的资本存量和 GDP。
```{.r}
# Solow 模型, y, i, k 为起始值
solow <- function(A, l, s, p_func, y, i, k) {
    solow_iter <- function(idx, y, k, i) {
        i[idx+1] <- y[idx] * s[idx]
        k[idx+1] <- k[idx] + i[idx+1]
        y[idx+1] <- p_func(A=A[idx+1], k=k[idx+1], l=l[idx+1])
        if (length(A) <= idx+1) {
            data.frame(y, k, i)
        } else {
            solow_iter(idx+1, y=y, k=k, i=i)
        }
    }
    solow_iter(1, y=y, k=k, i=i)
}

# 模拟出后续年份的 GDP, K
p_func <- production_function(coefs=coefs, beta_0=coefs["beta_0"])
data_simulated <- solow(A=A, l=l, s=s_simulated,
                        p_func=p_func, y=gdp[1], i=NA, k=k[1])
```

模型模拟出的GDP $Y$，资本存量 $K$，投资（下一期）$I$：
```{.r}
stargazer(data_simulated, type="text", covariate.labels=c("Y", "K", "I"))
```

```{.r}
gdp_simulated <- data_simulated$y
k_simulated <- data_simulated$k
simulation["gdp"] = gdp
simulation["gdp_simulated"] = gdp_simulated
simulation["k"] = k
simulation["k_simulated"] = k_simulated
dd_sub <- simulation[, c("year", "gdp", "gdp_simulated", "k", "k_simulated")]
dd <- melt(dd_sub, id=c("year"))
p <- ggplot(dd, aes(year, value, color=variable)) + geom_line()
p + labs(title="GDP 和资本存量的模拟",
         x="年份", y="GDP 或资本存量(亿元)") +
    scale_color_discrete(labels=c("GDP 真实值", "GDP 模拟值", "资本存量真实值", "资本存量模拟值")) +
    theme(legend.title=element_blank())
```

模拟出的 GDP 和资本存量都与真实值十分相近。

### 劳动者的人均产出和实际工资的模拟 Simulation of GDP Per Worker and Real Wage
人均产出由 GDP 除以就业人数得到，实际工资由公式 $w=\phi_L\frac{Y}{L}$ 得到，真实的实际工资由真实的劳动要素占比和真实的 GDP 计算得来，模拟的实际工资由模拟的劳动要素占比和模拟的 GDP 得来。
```{.r}
# 劳动者的人均产出，单位元
gdp_per_worker <- (gdp * 100000000) / (l * 10000)
simulation["gdp_per_worker"] <- gdp_per_worker
gdp_per_worker_simulated <- (data_simulated$y * 100000000) / (l * 10000)
simulation["gdp_per_worker_simulated"] <- gdp_per_worker_simulated

# 实际工资，单位元，不是工资率
wage_rate <- function(phi_l, y, l) {
    phi_l * ((y * 100000000)/ (l*10000))
}
wage <- wage_rate(phi_l=phi_l, y=gdp, l=l)
wage_simulated <- wage_rate(phi_l=phi_l_simulated, y=gdp_simulated,l=l)
simulation["wage"] = wage
simulation["wage_simulated"] = wage_simulated
dd_sub <- simulation[, c("year", "gdp_per_worker", "gdp_per_worker_simulated",
                         "wage", "wage_simulated")]
dd <- melt(dd_sub, id=c("year"))
p <- ggplot(dd)
p + geom_line(aes(year, value, color=variable)) +
    labs(title="人均产出与实际工资模拟",
         x="年份", y="人均产出或实际工资(元)") +
    theme(legend.title=element_blank()) +
    scale_color_discrete(labels=c("人均产出真实值", "人均产出模拟值",
                                  "实际工资真实值", "实际工资模拟值"))
```

从图可以看出，劳动者的人均产出和实际工资都能很好地模拟。

### 资本收益率 Capital Profit Rate
资本收益率由 $i = \phi_K \frac{Y}{K}$ 得到，真实的资本收益率由真实的资本收入占比、真实的 GDP 和真实的资本存量得来，模拟的资本收益率由模拟的资本收入占比、模拟的 GDP 和模拟的资本存量得来。
```{.r}
# 资本收益率
interest_rate_f <- function(phi_k, y, k) {
    phi_k * (y) / (k)
}

# 真实的资本收益率
interest_rate <- interest_rate_f(phi_k, y=gdp, k=k)
interest_rate_simulated <- interest_rate_f(phi_k=phi_k_simulated,
                                           y=gdp_simulated,
                                           k=k_simulated)
simulation["interest_rate"] <- interest_rate
simulation["interest_rate_simulated"] <- interest_rate_simulated

dd_sub <- simulation[, c("year", "interest_rate", "interest_rate_simulated")]
dd <- melt(dd_sub, id=c("year"))
p <- ggplot(dd)
p + geom_line(aes(year, value, color=variable)) +
    labs(title="资本收益率模拟",
         x="年份", y="资本收益率") +
    theme(legend.title=element_blank()) +
    scale_color_discrete(labels=c("资本收益率真实值", "资本收益率模拟值"))
```

# 小结
模型能够很好地模拟出中国在 1982 至 2009 年的经济情况，甚至超越对数生产函数计算出的 GDP 与真实值的差距大部分在0.2% 以内，模拟的资本存量、人均产出、实际工资、资本收益率都与真实值一致。

但是超越对数生产函数的准确性依赖于不断调整出来的全要素生产率 $A$，如果不能知道准确的全要素生产率，这个模型的解释能力就会大大下降，怪不得 Allen 研究的是经济史问题。

这篇文章不是一篇论文，没有什么要论证的，主要是为了完成老师布置的任务，本来没想到要做的，但是老师现在回学校了，万一问起我进度，如果我没做的话可能会很麻烦。

最开始准备用 Python 做模拟，但是我对 Python 的科学计算库 Numpy 和统计库 Pandas 不是很熟，反正都不熟，于是就选择了专业的 R 语言。因为不熟练，不会写单元测试，很多 Bug 在出现很久之后才发现，然后就是几个小时几个小时的 Debug。

写这篇文章的过程中，最大的障碍是不断迭代不断调整求出那个超越对数生产函数，这个程序本身好写，关键是不好做测试，我根本不知道最后的结果应该是什么，每次我都只能把循环次数限定在 1000 次以内，然后从几万行的输出结果里找哪里出了问题。这个求超越对数生产函数的程序一个上午就写完了，却花了 6 天时间找出所有的 Bug，最后的一个 Bug 花了我半天时间，仅仅是因为一个括号移位了。

这一篇文章让我终于有机会好好使用 R 语言，学了 ggplot2、knitr、reshape2 等等库，收获还是很大的。

[ ] Allen Engels' Pause

[1] 赵志耘, 杨朝峰. 中国全要素生产率的测算与解释: 1979—2009 年[j]. 财经问题研究, 2011.9

[ ] 韩雷. 中国劳动收入占比变化的制度解释

