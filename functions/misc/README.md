# Miscellaneous

This section contains some tips and tricks for making your life easier while writing python.  Python uses some elements of [functional programming] (https://en.wikipedia.org/wiki/Functional_programming) as well as [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), but the end result is a rich language that is meant to have one-liner solutions for most simple tasks.

My advice is: take advantage of them!

**Personal note**: I think [list comprehensions](#list-comprehensions) are one of the coolest things that python has to offer that a lot of newcomers don't know about.  If you like, skip down to that section to see some really awesome tricks!

## Iterating over iterables

Many types of objects are iterable (strings, lists, dictionaries, tuples, files, etc), and if you are not used to pythonic iteration, you may do something like this:

```python
for i in range(0, len(mylist)):
    print(mylist[i])
```

...and that works.  It's just not very pythonic.

Instead, consider this:

```python
for item in mylist:
    print(item)
```

Python automatically assigns the values in `mylist` to the variable `item`.  We don't even need to know the indices involved!

...but what if we do?  It's frequently the case that you need access to those indices.  For those cases, use this:

```python
for index, item in enumerate(mylist):
    print("Index:", index)
    print("Value:", item)
```

The `enumerate` function is a builtin in that returns a list of tuples of the form `(index, value)` for each value in the iterable object.

*However*, if the reason you need the index is to access another list of the same length... (i.e., like the following example):

```python
A = [2, 3, 5, 7, 11]
B = [13, 17, 19, 21, 23]
for index, item_a in enumerate(A):
    item_b = B[index]
    print(item_a, item_b)
```

...consider using the `zip` function!  (Covered in section [builtins](#builtins)).

```python
A = [2, 3, 5, 7, 11]
B = [13, 17, 19, 21, 23]
for item_a, item_b in zip(A, B):
    print(item_a, item_b)
```

## Iterators

I was sort of hoping to avoid having to describe what an *iterator* is, but alas, it keeps coming up.

An *iterator* is an object that you use to iterate over iterables...

Ahem.  An example is probably in order.

Suppose I, for some reason, need a giant list.  So giant that it won't all fit in memory (maybe a list with several billion ints or something).

Since we don't *need* to store the whole list in memory at the same time, we could use an *iterator*.

You rarely need to create iterators yourself, so this section is only here to provide a brief definition and an example (this example is specifically python3.  For python2, you would use `xrange`):

```python
R = range(1000000000)
for num in R:
    if num == 42000:
        print(num)
```


The `range` object is an iterator that allows us to iterate from 0 to 999999999 without having to store all the numbers in memory.

(Think of it like this: in order to count from 1 to a billion, all you need to keep track of is what number you're on.  Whatever number you're on, just add 1 to get to the next one).

## Builtins

Here are several builtin functions to reduce the clutter in your life.

### map

The `map` function applies a function to all the elements in an iterable object.  It returns an *iterator* (that is, we can iterate over it, but it's not a list),

```python
def f(x):
    return x**2

nums = [2, 3, 5, 7, 11]

map_obj = map(f, nums)
for m in map_obj:
    print(m)
# 4
# 9
# 25
# 49
# 121
```

Of course, this is a perfect time to use a [lambda](../basics#lambdas)!

```python
nums = [2, 3, 5, 7, 11]

for m in map(lambda x: x**2, nums):
    print(m)
# 4
# 9
# 25
# 49
# 121
```

### zip

We saw an example of `zip` earlier, but what it does specifically is this:
 - Take several iterable objects
 - Create an iterator of tuples where each tuple contains the elements from each iterable object in that particular position

This is easier to explain with an example:


```python
A = ["a", "b", "c"]
B = [True, False, True]
N = [1, 2, 3]

zip_obj = zip(A, B, N)
for z in zip_obj:
    print(z)
# ('a', True, 1)
# ('b', False, 2)
# ('c', True, 3)
```

### filter

The `filter` builtin will take a function and an iterable, and return an iterator over the elements in the iterable that elicit a return value of `True` when passed to the function.

Example (I'm going to start just using lambdas when appropriate now):

```python

filter_obj = filter(lambda x: x > 5, [2, 4, 6, 8, 10])
for f in filter_obj:
    print(f)
# 6
# 8
# 10
```

### any

The `any` builtin will take an iterable object and return `True` if any of the elements are `True` (or *truthy*), and `False` otherwise.

```python
print(any([0, 0, 0, 1, 0]))
# True

print(any(["", "", "", 0]))
# False
```

Often, we combine `map` with `any` to analyze data.

Example: *Are any of these numbers bigger than 10?*

```python
L = [2, 4, 6, 8, 10, 12, 14]
print(any(map(lambda x: x > 10, L)))
# True
```

### all

The `all` builtin will take an iterable object and return `True` if all of the elements are `True` (or *truthy*), and `False` otherwise.

```python
print(all([0, 0, 0, 1, 0]))
# False

print(all([1, 1, 1, 1, "a"))
# True
```

Again, we can combine `map` with `all` to analyze data.

Example: *Are all of these numbers bigger than 10?*

```python
L = [2, 4, 6, 8, 10, 12, 14]
print(all(map(lambda x: x > 10, L)))
# False
```

## Generators

A *generator* is a great little way to make your own iterators.

Here we introduce the `yield` keyword that lets the function you define know that it should behave like an iterator.

Example (notice the `__next__` function):

```python
def fib_gen():
    a = 1
    b = 1
    while 1:
        save = a
        a = a + b
        b = save
        yield b

F = fib_gen()
for i in range(10):
    print(F.__next__())
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
```
    
Notice also that our generator is (seemingly) infinite.  It will continue yielding values forever (which is why we cut it off after 10).  Here's an example that lets you stop your generator when it should stop generating values:

```python
def fib_gen_short():
    a = 1
    b = 1
    while 1:
        save = a
        a = a + b
        b = save
        yield b
        if b > 100:
            raise StopIteration

F = fib_gen_short()
for num in F:
    print(num)
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
```

## List Comprehensions

Oh boy!  My favorite.

*List comprehensions* are a wonderful, beautiful tool that will instantly start reducing unnecessary verbosity and repetition in your code, making it shorter and easier to read.

First, a case study.  The goal is to take the list of numbers from 1 to 10, and iterate over them, creating a shortlist of the squares of only the even numbers.  Let's watch, shall we?

**Attempt #1**

```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
short = []
for num in L:
    if num%2 == 0:
        short.append(num**2)
print(short)
# [4, 16, 36, 64, 100]
```

Well, this accomplishes the task, surely.  On the other hand, this also sounds like a task suited for `filter` and `map`:

**Attempt #2**

```python 
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
short = []
for num in map(lambda x: x**2, filter(lambda x: x%2 == 0, L)):
    short.append(num)
print(short)
# [4, 16, 36, 64, 100]
```

It works.  It's one line shorter.  But it ends up containing nested functions (`map` and `filter`) which, while correct, make the code hard to read.

Enter: the *list comprehension*.

We'll start with an example, and then dissect the details.

**Attempt #3**

```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
short = [x**2 for x in L if x%2 == 0]
print(short)
# [4, 16, 36, 64, 100]
```

Voila!  We have shaved off *two more lines* and the code is more readable than ever (depending on one's ability to comprehend a list comprehension...).

Here's the line we want to pull apart:

`short = [x**2 for x in L if x%2 == 0]`

It is likely that this is your first time seeing anything like this.

Let's start with this: a *list comprehension* is a statement for building a list using iteration.

Given that definition, let's take a look at a simpler example:

```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
short = [x**2 for x in L]
print(short)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

We have built the `short` list from `L` using the statement `[x**2 for x in L]`.  The `for x in L` describes the iteration, and `x**2` describes the elements that shall be placed in the new list.

It is equivalent to:

```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
short = []
for x in L:
    short.append(x**2)
```

Since this particular type of iteration is so commonplace, list comprehensions are a pleasingly brief shortcut.

Now, going back to our first list comprehension example, we also gave a condition:

`[x**2 for x in L if x%2 == 0]`

This is equivalent to:

```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
short = []
for x in L:
    if x%2 == 0:
        short.append(x**2)
```

The general form of a list comprehension is as follows:

`[{element} {loop} {condition}]`

Here are a few more examples to showcase the power and flexibility of list comprehensions:

```python
# Given a list of dictionaries, extract the value associated with the key "name" in each dictionary
names = [dict["name"] for dict in dict_list]

# Filter out all lines from a file starting with "#"
good_lines = [line for line in file_obj if line.startswith("#")]

# Flatten a nested list
nest = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for each_list in nest for x in each_list]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This last one was a curve ball!  Yes, it turns out you can do nested iteration *all on one line*.  Just make sure that the iteration you normally do top to bottom now goes left to right.

That is, this:
```python
for each_list in nest for x in each_list
```

is equivalent to this:
```python
for each_list in nest:
    for x in each_list:
```
