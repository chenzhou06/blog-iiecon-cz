Title: Note on Introductory Econometric (Wooldridge) -- Chapter 4
Author: Chen Zhou
Date: 2015-10-11 10:00
Tags: economics, learning
Category: Economics

Sampling Distributions of the OLS Estimators
============================================

\[MLR.6 Normality\] The population error $u$ is independent of the
explanatory variables $x_1,
  x_2, \ldots, x_k$ and is normally distributed with zero mean and
variance $\sigma^2$: $u~Normal(0,\sigma^2)$.

Gauss-Markov assumptions plus the assumption of a normally distributed
error term is the so-called *classical linear model (CLM) assumptions*

The population assumptions of the CLM is
$$y|\mathbf{x} \sim \mathrm{Normal}(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k, \sigma^2)$$

In many cases normality is not a good assumption, so using a
transformation yields a distribution that is closer to normal. In other
cases, the MLR.6 is clearly false.

\[Normal Sampling Distributions\] Under the CLM assumptions MLR.1
through MLR.6, conditional on the sample values of the independent
variables,
$$\hat{\beta_j} = \mathrm{Normal} [\beta_j,\mathrm{Var}(\hat{\beta_j})],$$
where $\mathrm{Var}(\hat{beta_j})$ was given in Chapter 3. Therefore,
$$(\hat{\beta_j}-\beta_j) / \mathrm{sd}(\hat{\beta_j}) \sim \mathrm{Normal}(0,1).$$

Each $\hat{\beta}_j$ can be written as
$$\hat{\beta}_j = \beta_j + \sum_{i=1}^n w_{ij} u_i$$ where
$w_{ij} = \hat{r}_{ij} / \mathrm{SSR}$; $\hat{r}_{ij}$ is the $i^{th}$
residual from the regression of the $x_i$ on all the other independent
variables, $\mathrm{SSR}_j$ is the sum of squared residuals from this
regression.

Sine the $w_{ij}$ depend only on the independent variables, they are
nonrandom. So $\hat{\beta}_j$ is a linear combination of the errors in
the sample. The errors are identically distributed
$\mathrm{Normal}(0, \sigma^2)$ (Assumption MLR.2). Because a linear
combination of such random variables is normally distributed. The proof
completed. When we standardize $\hat{\beta}_j$, the second part of this
theorem is reached.

Testing Hypotheses about a Single Population Parameter: The $t$ Test
====================================================================

\[$t$ distribution for the standardized estimators\]\[thrm:betadist\]
Under the CLM assumptions MLR.1 through MLR.6,
$$(\hat{\beta_j}-\beta_j)/se(\hat{\beta_j}) \sim t_{n-k-1} = t_{df}$$
where $k+1$ is the number of unknown parameters in the model
$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$ and $n-k-1$ is
the degrees of freedom ($df$).

Null hypothesis (Simple hypothesis) $$\mathrm{H_0}:\beta_j=0$$ means
$x_j$ has no effect on the expected value of $y$.

The $t$ statistic or ratio for simple hypotheses
$$t_{\hat{\beta_j}}=\frac{\hat{\beta_j}}{\mathrm{se}(\hat{\beta_j})}$$

Values of $t_{\hat{\beta_j}}$ sufficiently far from zero will result in
a rejection of $\mathrm{H_0}$.

Testing against One-Sided Alternatives
--------------------------------------

Consider a *one-sided* alternative of the form
$$\mathrm{H_1}:\beta_j > 0.$$

If the $t$ statistics is bigger than a *critical value* $c$,
$\mathrm{H_0}$ is rejected in favor of $\mathrm{H_1}$ at a significance
level. $$t_{\hat{\beta}_j} > c.$$

As the degrees of freedom in the $t$ distribution get large, the $t$
distribution approaches the standard normal distribution.

For degrees of distribution greater then 120, one can use the standard
normal critical values.

Two-Sided Alternatives
----------------------

Two-sided alternatives $$\mathrm{H_1}:\beta_j \ne 0.$$

Reject rule $$|t_{\hat{\beta}_j}| > c.$$ where $c$ is the percentile
level where the area in each tail of the $t$ distribution equal half of
the significance level.

Testing Other Hypotheses about $\beta_j$
----------------------------------------

The null is $$\mathrm{H_0}: \beta_j = a_j,$$ where $a_j$ is our
hypothesized value of $\mathrm{H_0}$. The $t$ statistic is
$$t = \frac{\hat{\beta}_j - a_j}{\mathrm{se}(\hat{\beta}_j)}.$$

Computing $p$-Value for $t$ Tests
---------------------------------

The $p$-value (the *smallest significance level* at which the null
hypothesis would be rejected) is $$\mathrm{P}(|T| > |t|),$$ where $T$ is
a $t$ distributed random variable with $n-k-1$ degrees of freedom, and
$t$ is the $t$ statistics.

We can obtain the one-sided $p$-value by just dividing the two-sided
$p$-value by 2.

A Reminder on the Language of Classical Hypothesis Testing
----------------------------------------------------------

When $\mathrm{H_0}$ is not rejected, we prefer to use the language “we
fail to reject $\mathrm{H_0}$ at the x% level”. It makes no sense to say
that we “accept” either of these hypotheses.

Economic, or Practical, versus Statistical Significance
-------------------------------------------------------

Guidelines for discussing the economic and statistical significance of a
variable in a multiple regression model, see figure \[guideline\].

[Guideline for discussing the economic and statistical significance of
a variable in multiple regression.<span
data-label="guideline"></span>](/pdfs/chapter4-guideline.pdf)

Confidence Intervals
====================

From the fact that
$\hat{\beta}_j - \beta_j/\mathrm{se}({\hat{\beta}}_j)$ in
Theorem \[thrm:betadist\], the *confidence interval* is given by
$${\hat{\beta}}_j \pm c\cdot \mathrm{se}({\hat{\beta}}_j),$$ where $c$
is the percentile level in a $t_{n-k-1}$ distribution.

Testing Hypotheses about a Single Linear Combination of the Parameters
----------------------------------------------------------------------

Consider a simple model
$$\log(wage) = \beta_0 + \beta_1 jc + \beta_2 univ + \beta_3 exper + u,$$

The hypothesis is $$\mathrm{H_0}:\beta_1 = \beta_2,$$ The alternative
$$\mathrm{H_1}:\beta_1 < \beta_2.$$

We rewrite the null and alternative as
$$\mathrm{H_0}: \beta_1 - \beta_2 = 0,$$
$$\mathrm{H_1}: \beta_1 - \beta_2 < 0.$$

The $t$ statistic based on the estimated difference
${\hat{\beta}}_1 - {\hat{\beta}}_2$ $$\label{eq:bbt}
    t = \frac{{\hat{\beta}}_1 - {\hat{\beta}}_2}{\mathrm{se}({\hat{\beta}}_1 - {\hat{\beta}}_2)}.$$

Because the alternative is $\beta_1 < \beta_2$, the rejection rule is
$t < -c$, $c$ is the critical value based on significance level and
degree freedom.

The ${\hat{\beta}}_1 - {\hat{\beta}}_2$ can be derived from OLS.

The denominator of equation (\[eq:bbt\]) can be derived from
$${\mathrm{Var}}({\hat{\beta}}_1 - {\hat{\beta}}_2) = {\mathrm{Var}}({\hat{\beta}}_1) + {\mathrm{Var}}({\hat{\beta}}_2) - 2 {\mathrm{Cov} }({\hat{\beta}}_1, {\hat{\beta}}_2).$$
So we have
$${\mathrm{se}}({\hat{\beta}}_1 - {\hat{\beta}}_2) = \left\lbrace  {\left[ se({\hat{\beta}}_1) \right]} ^2 + {\left[ se({\hat{\beta}}_2)\right]} ^2 - 2 s_{12} \right\rbrace ^{1/2},$$
where $s_{12}$ denotes an estimate of
${\mathrm{Cov} }({\hat{\beta}}_1, {\hat{\beta}}_2)$.

Another way to test the hypotheses is to estimate a different model in
which we define a new parameter $\theta_1 = \beta_1 - \beta_2$, the test
$${\mathrm{H_0}}: \theta_1 = 0~\mathrm{against}~{\mathrm{H_1}}: \theta_1 < 0,$$
then the model can be rewritten as $$\begin{split}
        \log(wage) & = \beta_0 + (\theta_1 + \beta_2)jc + \beta_2 univ + \beta_3 exper + u \\
                   & = \beta_0 + \theta_1 jc + \beta_2 (jc + univ) + \beta_3 exper + u
    \end{split}$$

Testing Multiple Linear Restrictions: The $F$ Test
==================================================

Testing Exclusion Restrictions
------------------------------

We want to test whether a group of variables has no effect on the
dependent variable. Consider the model
$$\log(salary) = \beta_0 + \beta_1 years + \beta_2 gamesyr + \beta_3 bavg + \beta_4 hunsys + \beta_5 rbisyr + u.$$
The null hypothesis is
$${\mathrm{H_0}}: \beta_3 = 0, \beta_4 = 0, \beta_5 = 0.$$ The
alternative is
$${\mathrm{H_1}}: {\mathrm{H_0}}~\text{is not true}$$ We do not have enough
statistical background about the form of the alternative.

These are *exclusion restrictions* and this is an example of a set of
*multiple restrictions*. A test of multiple restrictions is called a
*multiple hypotheses test* or a *joint hypotheses test*.

In general, there are some steps to perform a multiple hypotheses test:

-   Testing the model without variables in the null hypotheses, known as
    *restricted model*;

-   Estimate the *unrestricted model*;

-   Calculate the $F$ statistic.

We write unrestricted model at first
$$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$$ and suppose we
have $q$ exclusion restrictions to test, the null hypotheses is
$${\mathrm{H_0}}: \beta_{k-q+1} = 0, \ldots , \beta_k = 0.$$

Then impose the restrictions under ${\mathrm{H_0}}$, we are left with
the *restricted model* $$\begin{aligned}
    y = \beta_0 + \beta_1 x_1 + \cdots + \beta_{k-q} x_{k-q} + u.\end{aligned}$$

The $F$ statistic is defined by
$$F = \frac{\left( \mathrm{SSR}_r - \mathrm{SSR}_{ur} \right)  / q}{\mathrm{SSR}_{ur} / \left( n-k-1 \right)}$$
where $$\begin{split}
        & \mathrm{SSR}_r~\text{is the sum of squared residuals from the restricted model}; \\
        & \mathrm{SSR}_{ur}~\text{is the sum of squared residuals from the unrestricted model.}
    \end{split}$$

Notice that $\mathrm{SSR}_r$ can be no smaller than $\mathrm{SSR}_{ur}$,
the $F$ statistic is *always nonnegative*.

We can think $F$ statistic as measuring the relative increase in
$\mathrm{SSR}$ when moving from the unrestricted to the restricted
model.

The number of independent variables that are dropped is $q$
$$\begin{split}
        q & =  \text{numerator degrees of freedom} \\
          & = df_r - df_{ur} \\
        n - k - 1 & =~\text{denominator degrees of freedom} \\
                  & = df_{ur}
    \end{split}$$

Using the fact that $\mathrm{SSR}_r = \mathrm{SST}(1 - R^2)$ and
$\mathrm{SSR}_{ur} = \mathrm{SST}(1-R^2_{ur})$, $$\begin{split}
        F & = \frac{(R^2_{ur} - R^2_r) / q}{(1-R^2_{ur})/(n-k-1)} \\
    & = \frac{(R^2_{ur} - R^2_r) / q}{(1-R^2_{ur}) / df_{ur}}
    \end{split}$$

Computing $p$-value for $F$ Tests
---------------------------------

$$p\text{-value} = \mathrm{P}(\mathscr{F} > F)$$

It is the probability of observing a value of $F$ at least as large as
we did, given that the null hypotheses is true.

The $F$ statistic for Overall Significance of a Regression
----------------------------------------------------------

The restricted model $$y = \beta_0 + u~(R^2 = 0)$$

The $F$ statistic $$\begin{aligned}
    {R^2 / k \over (1-R^2)/(n-k-1)}\end{aligned}$$ called the overall
significance of the regression.

Testing General Linear Restrictions
-----------------------------------

Null hypothesis

$${\mathrm{H_0}}: \beta_1 = 1, \beta_2 = 0, \beta_3 = 0, \beta_4 = 0.$$

Unrestricted model
$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + \beta_4 x_4 + u$$

Restricted model $$\label{eq:rm}
    y = \beta_0 + x_1 + u$$

To impose the restriction that $\beta_1 = 1$, rewrite equation
(\[eq:rm\]) as $$\label{eq:rw}
    y - x_1 = \beta_0 + u$$ We cannot use the $R^2$ form of the $F$
statistic for this example because the dependent variable in  is
different from the one in . This means the total sum of squares from the
two regressions will be different.
