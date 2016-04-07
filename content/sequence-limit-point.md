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

Python provides a convenient way to overload the brackets operator. We can add a
`__getitem__` method to our `myseq` class to use this feature. However, if we
care about the efficiency, `myseq` class should not generate a sequence from
start to end for every query. For example, we want the 10th number in the
sequence, the first time the class iterates 10 times to generate the 10th
number. In this process every index between them should be calculated once and
cached. From then on, for every query at $i$th index, if $i <= 10$, the class
needs not to go through the process again, it just returns the value in the
cache.

To implement these ideas, `myseq` has a new property `cache` which is a list
storing values calculated. The `__getitem__` method is recursive, first it
compares the index and the length of cache. If the cache is longer than the
index, which means the wanted value has been calculated, the cached value is
returned. No extra iteration is invoked. Otherwise, the `__getitem__` is invoked
again on a smaller index and the iteration advances one more step updating its
cache. Once the index is equal to the length of cache, the $n$th value is
returned.

``` python
class myseq(object):
	def __init__(self, group_max, group_number=0):
		self.group_number = group_number
		self.current = 0
		self.group_max = group_max - 1
		self.cache = [1]

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
		self.cache.append(self.current)
		return self.current

	def __getitem__(self, n):
		if not isinstance(n, int): raise TypeError
		offset = n - len(self.cache)
		if offset <= 0:
			return self.cache[n]
		else:
			try:
				self.__next__()
			except StopIteration:
				raise IndexError
			else:
				self.__getitem__(n-1)
```
