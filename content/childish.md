Title: Childish Math
Date: 2015-05-12
Category: Mathematics
Tags: math, learning

When I was studying the GRE Offical Guide, I came across some very primitive
theoroms about integers. 

* The sum of two even integers is an even integer.
* The sum of two odd integers is an even integer.
* The sum of an even integer and an odd integer is an odd integer.
* The product of two even integers is an even integer.
* The product of two odd integers is an odd integer.
* The production of an even integer and an odd integer is an even integer.

To escape from the demanding task of reading books, I tried to prove them for
fun.

First, what makes an integer even or odd?

Even Integer
:   If an integer is divisible by 2, it is called an **even integer**.
Odd Integer
:   Otherwise it is an **odd integer**.

Let's start!

## The sum of two even integers is an even integer

Assume $a$ and $b$ are both even integer, then $a$ is divisible by 2, 
$b$ is divisible by 2. The sum of $a$ and $b$ -- $a + b$ alse is divisible by 2,
because $(a + b) / 2 = a/2 + b/2$. There is no remainder of $(a + b)/2$. The first theorom is proved.

## The sum of two odd integers is an even integer

Because any odd integer can be represented as an even integer plus one,
odd integer $c$ and $d$ can be represented as $a + 1$ and $b + 1$ respectively,
and $a$ and $b$ are even integer.

So, sum of $c$ and $d$ equals to $(a+1) + (b+1)$, which can be written as
$a + b + 2$. Apparently, sum of even integers is still even integer.

## The sum of an even integer and an odd integer is an odd integer

The sum of an odd integer $c$ plus an even integer $a$ is as same as
the sum of an odd integer $d+1$ plus an even integer $a$, where $b+1$ equals $c$
and $b$ is even. So, $c+a$ is equal to $b + a + 1$ which turns out to be an odd
integer.

## The product of two even integers is an even integer

The product of two even integers $a$ and $b$ -- $ab$ is the same as the sum of
$b$ amount of $a$. Due to the fact that the sum of two even integers is even,
we can easily conclude that no matter what number of even integers is added,
the sum of them is even. The product of two even integers is even accordingly.  

## The product of two odd integers is an odd integer

The product of two odd integers $c$ and $d$ can be expressed with two even
integers $a$ and $b$ -- $(a+1)(b+1)$, where $a + 1 = c, b + 1 = b$. 

$$
(a + 1)(b + 1) = ab + a + b + 1
$$

According to the theorom which has been proved, the equation above inferred
that the product of two odd integers is odd ($ab+a+b$ is even, one added makes
it odd).

## The product of an even integer and an odd integer is an even integer

The product of an even integer $a$ and an odd integer $c$ can be written as

$$ac = a(b + 1)$$

where $b$ is even. Expand the left of the equation, 

$$ab + b$$ 

which becomes the sum of two even integers. The product of an even integer and
an odd integer is an even integer.

