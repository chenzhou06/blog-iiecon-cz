Title: Hash Functions
Author: Chen Zhou
Category: Programming
Tags: programming
Date: 2016-03-23 22:33:09
<!-- TODO
	Hash function usage.
	Hash function for string.
-->
Hash function can transform a key to an array index. If we have an array
that can hold $M$ key-value pairs, then we need a function that can
transform any given key into an index into that array: an integer in the
range $[0, M-1]$ [^1].

[^1]: This definition is adopted from
	[here](http://algs4.cs.princeton.edu/34hash/).

The key can be one of different types:

* Positive integer;
* Floating-point numbers;
* Strings;
* Compound keys.

If the key is a positive integer, the most basic hash function can
make a modular out of that key, which is called **modular hashing**.
A possible Python implementation can be written as

```python
def hash_modular(integar):
	hash = 31
	return integar % hash

hash_modular(100)
# => 7
```

The `hash_modular` function returns the remainder when dividing
`integar` by `hash` which is set to 31. So this function can
transform any key to an array index ranged from 0 to 30.

For the sake of practicing, I try to write this algorithm in
multiple languages.

### Racket
```racket
#lang racket/base

(define (hash-modular integar)
  (let ([capacity 31])
	(remainder integar capacity)))

(displayln (hash-modular 100))
;; => 7
```
### C++
```c++
#include <iostream>

int hash_modular(int n) {
	int capacity = 31;
	return n % capacity;
}

int main() {
	std::cout << hash_modular(100) << std::endl;
}
```
