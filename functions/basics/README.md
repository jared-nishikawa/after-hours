# Basics

## Review

Functions
  - Can have inputs (one or more, or none)
  - Can have outputs (one or more, or none)
  - Can perform operations before returning output (once `return` is called, the function halts execution and returns control to the code that called it)

Examples:
~~~~
# One input, one output
def squared(x):
    return x**2

# Two inputs, one output
def square_add(x,y):
    return x**2 + y**2

# One input, two outputs
def square_cube(x):
    return x**2, x**3

# More complicated
def geometric(a, n):
    running_total = 0
    for i in range(n):
        running_total += a**i
    return running_total
~~~~

## Argument Type

Consider the following example
~~~~
def check_list(mylist):
    for item in mylist:
        if item == 0:
            print("Found a zero!")
~~~~

What do you think would happen if you tried `check_list(42)`? 

<details> 
  <summary>Show answer:</summary>
   `TypeError: 'int' object is not iterable`
</details>

This is because Python is not **strongly typed**.

In a language like C, you would see something like this
~~~~
int age = 42;
~~~~

The reason is that the C compiler *must* know how much memory to allocate for your variable.

Python is more lax about this, and will simply attempt to iterate over the integer and, subsequently, fail at *run time*.

Side note: if we tried to iterate over an integer in C, it would fail at *compile time*.  C is [**strongly typed**](https://en.wikipedia.org/wiki/Strong_and_weak_typing).

Python is [**duck typed**](https://en.wikipedia.org/wiki/Duck_typing).  ("If it walks like a duck and it quacks like a duck, then it must be a duck").

What this means is that regardless of what variables we pass to `check_list` as long as it's iterable (lists, strings, dicts, tuples, etc.) then the code will run.

## Functions can be arguments too...

There are a few great builtin functions like `map, all, any, filter, sum, sorted` (and more) that are worth experimenting with.

One of my favorites is `map`.

Probably the best way to explain `map` is to use an example.
```python
def squared(x):
    return x**2

nums = [0,1,2,3]

mapped = map(squared, nums)

for num in mapped:
    print(num)
```

## Lambdas

## Named Arguments

## Args and Kwargs
