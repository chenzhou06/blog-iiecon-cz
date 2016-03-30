Title: Basics of Probability Theory (part I)
Author: Chen Zhou
Category: Mathematics
Tags:  Mathematics
Date: 2016-03-30 21:48:14

The base of modern probability theory is built on Kolmogorov's work. Among them
the most important contribution is the Axioms of Probability (or the Kolmogorov
Axioms).

These axioms can be formally stated as

>	Given a sample space $S$ and an associated sigma algebra $\mathcal{B}$[^1], a
>	*probability function* is a function $P$ with domain $\mathcal{B}$ that
>	satisfies
>
>	1. $P(A) \ge 0$ for all $A \in \mathcal{B}$.
>	2. $P(S) = 1$.
>	3. If $A_1, A_2, \ldots \in \mathcal{B}$ are pairwise disjoint, then
>	   $P(\bigcup_{i=1}^\infty A_i) = \sum_{i=1}^\infty P(A_i)$.

[^1]: For the time being we leave sigma algebra unexplained.

So the Axioms of Probability is about probability functions. The funny part of
these axioms is that

>	Any function $P$ that satisfies the Axioms of Probability is called a
>	probability function.

The fact that there multiple ways to define a probability function really
terrified me once. Since that time I started doubting my intuitive thoughts on
tagging an outcome of random experiment with a fraction as its probability.

My worry was unnecessary according the following theorem which gives a common
method of defining a legitimate probability function.

>Let $S = {S_1, \ldots, S_n}$ be a finite set. Let $\mathcal{B}$ be any sigma
>algebra of subsets of $S$. Let $p_1, \ldots, p_n$ be non negative numbers that
>sum to 1. For any $A \in \mathcal{B}$, define $P(A)$ by

>$$ P(A) = \sum_{i:s_i \in A} p_i.$$

>Then $P$ is a probability function on $\mathcal{B}$ This remains true if $S =
>{s_1, s_2, \ldots} is a countable set.

This theorem legitimates our intuitive way of defining probability
function. Because it just gives a mathematical description of what we do in real
life to calculate probability of a random event.
