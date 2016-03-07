Title: Symbol of Sums
Author: Chen Zhou
Date: 2015-11-19
Category: Mathematics
Tags: math
Status: draft

Since I am pursuing my Master career, It is natural supposing me
familiar with the symbol of sums $\sum$ which I am actually not.

Today, when I was reading *The Art of Computer Programming* Chapter 1,
I finally understood some mechanism the symbol follows.

First, **the distributive law**, for products of sums:
$$
\left( \sum_{R(i)}a_i \right) \left( \sum_{S{j)} b_j \right) =
\sum_{R(i)} \left( \sum_{S(j)} a_i b_j  \right)
$$.

Many times when I was encountered with this product of sums, I was
just ignoring them pretending it is trifling. This time I figured
out that it just a sum of crossproduct of $a_i$ and $b_j$.

Second, **Change of variable**:
$$
\sum_{R(i)} a_i = \sum_{R(j)} a_j = \sum_{R(p(j))} a_{p(j)}.
$$

The book provides a more understandable example:
$$
\sum_{1\le j \le n} a_j = \sum_{1\le j-1 \le n} a_{j-1} =
\sum_{2\le j \le n+1} a_{j-1}.
$$

At the first time, one might be confused by the change the variable.
The middle item is easy to understand once we treat $j-1$ as a
whole. Also, we can just assign $i=j-1$ so that
$$
\sum_{1\le j-1 \le n} a_{j-1} = \sum_{1\le i \le n} a_i.
$$

The item at the right hand demands more thinking. Ask yourself, if
$2\le j \le n+1$, then what is the range of $j-1$? Within a second, we
shall know $1\e j-1 \le n$ which makes the right item the same as the
middle item.

A more demanding formula is
$$ \sum_{i=1}^n \sum_{j=1}^n a_{ij} =
\sum_{j=1}^n \sum_{i=j}^n a_{ij}.  $$

However, if we write down the
constriction of the left sum in a familiar way which turns out to be
$1\e j \le i \le n$, we can easily translate this relationship into
$1\le j \e n$ and $j \le i \le n$ which is just what the right sum
means.
