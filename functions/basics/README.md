# Basics

## Review

Functions
  - Can have inputs (one or more, or none)
  - Can have outputs (one or more, or none)
  - Can perform operations before returning output (once `return` is called, the function halts execution and returns control to the code that called it)

Examples:
```python
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
```

## Argument Type

Consider the following example
```python
def check_list(mylist):
    for item in mylist:
        if item == 0:
            print("Found a zero!")
```

What do you think would happen if you tried `check_list(42)`? 

<details> 
  <summary>Show answer:</summary>
   `TypeError: 'int' object is not iterable`
</details>

This is because Python is not **strongly typed**.

In a language like C, you would see something like this
```C
int age = 42;
```

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

mapped = map(squared, nums) # note how parentheses are not necessary when sending in the function squared as a parameter

for num in mapped:
    print(num)
> 0
> 1
> 4
> 9
```

## Lambdas

We frequently need a one-liner function for a single use (as in the last example).

It seems wasteful (or, for the initiated, *not pythonic*) to bother naming and saving the function when we know we'll never need it again.

For these sorts of cases, a **lambda** function will do the trick.

Lambdas provide a way to create quick-and-dirty functions without naming and saving them.

```python
nums = [0,1,2,3]

mapped = map(lambda x: x**2, nums)

for num in mapped:
    print(num)
> 0
> 1
> 4
> 9
```

**TODO**: cross-reference with class attributes

**TODO**: cross-reference with list comprehensions

## Named Arguments

New Python coders will often wonder to themselves "I have this function that needs eight parameters, but seven of them mostly are always the same.  I wish I could code in a *default* value so I don't have to muddy up my code with all this repeated information."

Wonder no longer!  It is possible with *named arguments* in your function.

Behold!

```python
def show_location(city, country, planet="Earth"):
    print("City:", city)
    print("Country:", country)
    print("Planet:", planet)

# See, you don't need to specify planet here
show_location("Boulder", "USA")
> City: Boulder
> Country: USA
> Planet: Earth

# But if you do want to change the planet parameter, you can!
show_location("Olympus Mons", "Amazonis", planet="Mars")
> City: Olympus Mons
> Country: Amazonis
> Planet: Mars
```

## Args and Kwargs

**Warning**: this confuses everyone.  If you don't get it the first time, don't worry too much.

Let's start with this
```python
print("Hello world!")
```

Now look at this
```python
print("Hello world!", "The weather is great!")
```

With me so far?
```python
print("Hello world!", "The weather is great!", "Mind the gap.")
```

See where I'm going with this?
```python
print("Hello world!", "The weather is great!", "Mind the gap.", "May the force be with you.")
```

Ok, one more, just for fun
```python
print("Hello world!", "The weather is great!", "Mind the gap.", "May the force be with you.", "Allons-y!")
```

What is the significance of this?  The `print` function can magically take as many parameters as you can throw at it?  That doesn't seem possible...

Consider this example as well
```python
# This is a function that takes a SINGLE argument
def display(somelist):
    for item in somelist:
        print(item)

display(["Hello world!", "The weather is great!", "Mind the gap."])
> Hello world!
> The weather is great!
> Mind the gap.
```

That's all well and good, but `print` is clearly taking *several* arguments, separated by commas, whereas this `display` function we just wrote takes a *single* argument which is a list.

The essential question is: "Can we write a function that can take an *arbitrary* number of arguments?"

The answer is yes!  Yes we can!

Check it out!
```python
def display(*args):
    for item in args:
        print(item)

display("Hello world!", "The weather is great!", "Mind the gap.")
> Hello world!
> The weather is great!
> Mind the gap.
```

Amazing!

And what if I want a function that will take arbitrary *named* arguments?

We can do that too!
```python
def display(*args, **kwargs):
    print("Args:")
    for arg in args:
        print(arg)

    print()

    print("Kwargs:")
    for key in kwargs.keys():
        print(key, kwargs[key])

display("Hello!", "World!", "Weather!", secret="Mind", msg="Gap")
> Args:
> Hello!
> World!
> Weather!
>
> Kwargs:
> secret Mind
> msg Gap
```

So it turns out that `*args` and `**kwargs` are special types of references that turn your function parameters into a list and a dictionary, respectively.

"args" = "arguments"

"kwargs" = "keyword arguments"

(It has nothing to do with [wargs](https://en.wikipedia.org/wiki/Warg), which is disappointing).


**TODO**: cross-reference with wrappers and decorators
