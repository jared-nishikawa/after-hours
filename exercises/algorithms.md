# Algorithms

University of Colorado - Boulder

CS 3104

Summer 2015

Book: *Algorithms* by Dasgupta, Papadimitriou, and Vazirani

https://www.amazon.com/Algorithms-Sanjoy-Dasgupta/dp/0073523402

## Assignment 1

### Problem 1

In each of the following situations, indicate whether $`f=O(g)`$, or $`f=\Omega(g)`$ or both (in which case $`f=\Theta(g)`$).

- $`f(n) = n^{1.01}, g(n) = n`$
- $`f(n) = \lg n, g(n) = \ln n`$
- $`f(n) = 2^n, g(n) = 3^n`$

### Problem 2

Compute the 200th Fibonacci number.

### Problem 3

Consider the following Python function:

```python
def find(a, target):
    x = 0
    y = len(a)
    while x < y:
        m = (x+y)/2
        if a[m] < target:
            x = m+1
        elif a[m] > target:
            y = m
        else:
            return m
    return -1
```

Suppose list $`a`$ has $`n`$ elements and is sorted.  USing $`\Theta()`$ notation, what is the best case running time as a funcction of $`n`$?  Using $`Theta()`$ notation, what is the worst case running time as a function of $`n`$?

### Problem 4

Modify the fund function from problem 4 by changing the 5th line from $`m=(x+y)/2`$ to $`m=(2*x+y)/3`$.  Now answer the same questions given in problem 3.
