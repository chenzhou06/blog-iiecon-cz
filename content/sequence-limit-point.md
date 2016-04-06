Title: A Sequence: 1,1,2,1,2,3,...
Author: Chen Zhou
Category: Programming, Mathematics
Tags: programming, mathematics
Date: 2016-04-06 18:54:48
Status: Draft

Definition of limit points. There are many sequences where every number can be a
limit point. One of them is

$$1,1,2,1,2,3,1,2,3,4,1,2,3,4,5, \ldots $$

This sequence can be split into groups $g_i = 1 \ldots i$. For example, $g_3$ is
$1,2,3$, and $g_4$ is $1,2,3,4$. So the sequence above can be viewed as

$$ g_1, g_2, g_3, g_4, \ldots $$

In Python we can write a class lazily generating this sequence.

``` python
class myseq(object):
	def __init__(self, group_max, group_number=0):
		self.group_number = group_number
		self.current = 0
		self.group_max = group_max

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.group_number:
			self.current = 1
			self.group_number += 1
		elif self.group_number > self.group_max:
			raise StopIteration
		else:
			self.current += 1
		return self.current
```

The `__iter__` method returns a iterable object which has `__next__`
method. Since this class has a `__next__` method, it just needs return itself.
Every time this object is iterated over, the `__next__` method will be invoked,
returning a number and updating its state.
