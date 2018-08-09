# Miscellaneous

This section contains some tips and tricks for making your life easier while writing python.  Python uses some elements of [functional programming] (https://en.wikipedia.org/wiki/Functional_programming) as well as [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), but the end result is a rich language that is meant to have one-liner solutions for most simple tasks.

My advice is: take advantage of them!

## Iterating over iterables

Many types of objects are iterable (strings, lists, dictionaries, tuples, files, etc), and if you are not used to pythonic iteration, you may do something like this:

```python
for i in range(0, len(mylist)):
    print(mylist[i])
```

...and that works.  It's just not very pythonic.

Instead, consider this:

```python
for item in mylist::
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

## Builtins
    map, zip, filter, any, all, reduce, 

## Generators

```python
for i in range(10):
    print(i)
```

## List Comprehensions

## Lambdas
