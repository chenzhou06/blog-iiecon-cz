Title: Note on Introductory Econometric (Wooldridge) -- Chapter 3
Author: Chen Zhou
Date: 2015-09-12 23:00
Tags: economics, learning
Category: Economics

Goodness-of-Fit
===============

$$R^2 = SSE / SST = 1 - \frac{SSR}{SST}$$

where

$$SST = \sum_{i=1}^n (y_i - \bar{y})^2$$
$$SSE = \sum_{i=1}^n (\hat{y_i} - \bar{y})^2$$
$$SSR = \sum_{i=1}^n u_i^2 = \sum_{i=1}^n (\hat{y_i} - y_i)^2$$

$R^2$ can be shown as the squared correlation as
$$R^2 = \frac{(\sum_{i=1}^n (y_i - \bar{y})(\hat{y_i} - \bar{y}))^2}{(\sum_{i=1}^n (y_i - \bar{y})^2)(\sum_{i=1}^n (\hat{y_i} - \bar{\hat{y}}))}$$

$R^2$ never decrease when any independent variable is added.

Regression though the Origin
----------------------------

$$\beta_0 = 0, \tilde{y} = \tilde{\beta_1} x_1 + \tilde{\beta_2} x_2 + \tilde{\beta_3} x_3 + \cdots + \tilde{\beta_k} x_k$$

The OLS residuals have no longer zero mean.

$R^2 = 1 - \frac{SSR}{SST}$ could be negative.

No set rule on computing $R^2$ for regression through the origin.

The Expected Value of the OLS Estimators
----------------------------------------

Assumptions:

MLR.1

:   Linear in Parameters.

MLR.2

:   Random Sampling.

MLR.3

:   No perfect Collinearity. It is allowed that the independent
    variables to be correlated. But the following cases are forbidden

    1.  One variable is a constant multiple of another

    2.  In elasticity function such as
        $\log(y) = \beta_0 + \beta_1 \log(x^2) + u$, the item
        $\log(x^2)$ and the item $\log(x)$ is perfect collinear.

    3.  One variable can be expressed as an exact linear function of
        other independent variables.

    4.  Sample size is too small, $n < k+1$, in which $n$ is the size of
        sample, $k$ is the number of parameters.

MLR.4

:   Zero Conditional Mean $$E(u|x_1, x_2, \dots, x_k) = 0$$ In the
    following situations, this assumption is failed to be fulfilled.

    -   The relationship between explained and explanatory
        is misspecified.

    -   Omitting an important factor.

    -   Measurement error in an explanatory variable.

Under assumptions MLR.1 through MLR.4, we can get unbiasedness of OLS
$$E(\hat{\beta_j}) = \beta_j, j = 0,1,\dots,k$$

Including Irrelevant variables in a Regression Model
----------------------------------------------------

It does not affect the unbiasedness of the OLS estimators.

Omitted Variable Bias
---------------------

Assume the population model is $$\label{eq:pop}
wage = \beta_0+\beta_1 educ+\beta_2 abil + u$$ We omit a variable $abil$
$$\label{eq:omited}
wage = \beta_0+\beta_1 educ+u$$ And we can get
$$\tilde{\beta_1} = \hat{\beta_1} + \hat{\beta_2}\tilde{\delta_1}$$
where $\tilde{\beta_1}$ is the coefficient in , $\hat{\beta_1}$ is the
coefficient in in . $\tilde{\delta_1}$ is the slop from
$\hat{educ} = \hat{\beta_0} + \hat{\beta_1} abil + u$. From above we can
get the bias
$$E(\tilde{\beta_1})=E(\hat{\beta_1}+\hat{\beta_2}\tilde{\delta_1})
=E(\hat{\beta_1})+E(\beta_2)\tilde{\delta_1}=\beta_1 + \beta_2\tilde{\delta_1}$$
So the bias
$$Bias(\tilde{\beta_1})=E(\tilde{\beta_1})-\beta_1 = \beta_2\tilde{\delta_1}$$
If $x_1$ and $x_2$ are unrelated, $\tilde{\beta_1}$ is unbiased. The
direction of this kind of bias can be referred in Table
\[tb:biasdirection\].

                $Corr(x_1, x_2)>0$   $Corr(x_1, x_2)$ &lt; 0
  ------------- -------------------- -------------------------
  $\beta_2>0$   Positive bias        Negative bias
  $\beta_2<0$   Negative bias        Positive bias

  : Summary of Bias<span data-label="tb:biasdirection"></span>

If we omit $x_3$ in
$$y=\beta_0+\beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + u$$ then get
$$\hat{y} = \hat{\beta_0} + \hat{\beta_1} x_1 + \hat{\beta_2} x_2$$ even
though $x_3$ is uncorrelated with $x_2$, $\hat{\beta_1}$ and
$\hat{\beta_2}$ are both biased. The direction of bias is also
uncertain. Assuming $x_3$ is unrelated with $x_2$, we can study the bias
of $\hat{\beta_1}$ by rules in Table \[tb:biasdirection\].

The Variance of the OLS Estimate
--------------------------------

Assumption MLR.5 homoskedasticity $$Var(u|x_1, \ldots, x_k)=\delta^2$$

MRL.1 through MRL.5 are known as Causs-Markov assumptions.

Sampling variances of the OLS Slope Estimators $$\label{eq:varbeta}
Var(\tilde{\beta_j})=\frac{\delta^2}{SST_j (1 - R_j^2)'}$$

The Components of the OLS Variance: Multicollinearity
-----------------------------------------------------

Three components:

The Error Variance, $\delta^2$

:   The greater the error variance, the greater the
    $Var(\hat{\beta_j})$, which can be easily be detected from .

The Total Sample Variation in $x_j, SST_j$

:   The greater the $SST_j$, the greater the $Var(\hat{\beta_j})$.

The Linear Relationship among the Independent Variables, $R_j^2$

:   The $R_j^2$, which is obtained from
    $x_j = \beta_0 + \beta_1 x_1 + \ldots + \beta_{j-1} x_j + u$, would
    increase the magnitude of $Var(\hat{\beta_j)}$.

Variances in Misspecified Models
--------------------------------

Following the detection before, we obtained two essential equations
$$Var(\hat{\beta_1}) = \delta^2 / [SST_1 (1 - R_1^2)]$$ and
$$Var(\hat{\beta_1}) = \delta^2 / SST_1$$

Two conclusions can be drawn

-   When $\beta_2 \neq 0$, $\tilde{\beta_1}$ is biased,
    $\hat{ \beta_1 }$ is unbiased, and
    $Var( \tilde{ \beta_1 } )<Var( \hat{\beta_1} )$.

-   When $\beta_2 = 0$, $\tilde{\beta_1}$ and $\hat{\beta_1}$ are both
    unbiased, and $Var(\tilde{\beta_1})<Var(\hat{\beta_1})$

Because the bias of $\tilde{ \beta_1 }$ does not shrink as the sample
size grews, while $Var(\tilde{\beta_1})$ and $Var(\hat{\beta_1})$ does.

Estimating $\sigma^2$: Standard Errors of the OLS Estimators
------------------------------------------------------------

$$\sigma^2 = E(u^2)$$

Estimating $\sigma^2$ by replacing $u_i$ with $\hat{u_i}$
$$\hat{\sigma}^2 = \frac{\left( \sum_{i=1}^n \hat{u}_i^2 \right) }{(n-k-1)}=\frac{SSR}{(n-k-1)}=SSR/df$$
where $df=n-(k+1)$ is the difference between the number of observations
and the number of estimated parameters.

The division by $df$ is due to the fact that $E(SSR)=(n-k-1)\sigma^2$.

To obtain the OLS estimates, $k+1$ restrictions are imposed on the OLS
residuals, $\sum_{i=1}^n u_i = 0, \sum_{i=1}^n x_ij \hat{u_i} = 0$, the
remainning $k+1$ residuals are known.

Under the Causs-Markov assumptions, $E(\hat{\sigma}^2)=\sigma^2$.
$\sigma^2$ is the standard error of the regression. It can either
decrease or increase when another independent variable is added, because
the $SSR$ is decreased along with $df=n-k-1$.
