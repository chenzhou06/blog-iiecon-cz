Title: Expectation: Minimizing Distance
Author: Chen Zhou
Category: Mathematics
Tags: math
Date: 2016-04-08 21:56:29

The expected value of a random variable $\mathrm{E}X$ can be viewed as a good
guess at a value $X$. We try to prove this by choosing a $b$ which minimizes
$\mathrm{E}(X-b)^2$ and provides us with a good predictor of $X$.

We first add a $\mathrm{E}X$ and minuses a $\mathrm{E}X$ to get

$$
\begin{align}
	\mathrm{E}(X-b)^2 & = \mathrm{E}(X - \mathrm{E}X + \mathrm{E}X - b)^2 \\
					  & = \mathrm{E}((X - \mathrm{E}X) + (\mathrm{E}X - b))^2 \\
					  & = \mathrm{E}(X - \mathrm{E}X)^2 + (\mathrm{E}X-b)^2
						  +2\mathrm{E}((X-\mathrm{E}X)(\mathrm{E}X-b)).
\end{align}
$$

Note that

$$
\mathrm{E}((X - \mathrm{E}X)(\mathrm{E}X-b)) =
(\mathrm{E}X - b)\mathrm{E}(X - \mathrm{E}X) = 0.
$$

This means that

$$ \mathrm{E}(X-b)^2 = \mathrm{E}(X-\mathrm{E}X)^2 + (\mathrm{E}X - b)^2. $$

We have no control over the first term on the right-hand side. The second term,
which is always greater than or equal to 0, can be made equal to 0 by choosing
$b = \mathrm{E}X$. Hence the best (closet) guess of $X$ is $\mathrm{E}X$.
