# Variables

## Mutable vs Immutable

An *immutable* object is an object whose state cannot be modified after it is created (https://en.wikipedia.org/wiki/Immutable_object).

But hold on:

```python
a = "hello"
print(a)
# hello

a = "world"
print(a)
# world
```

This is not the point we want to make with immutable object.  Remember, `a` is just the *name* of an object.  In the example above, we assigned to `a` two *different* objects.

With that in mind, try this on for size:

```python
a = "zello"
a[0] = "h"
# TypeError: 'str' object does not support item assignment
```

Aha!  We are now getting at the heart of the matter.  A string is an *immutable* object.  Once the internal values have been assigned, they cannot be changed.  (But the variable name `a` can be assigned to a different object).

For comparison:

```python
L = ['z', 'e', 'l', 'l', 'o']
L[0] = "h"
print(L)
['h', 'e', 'l', 'l', 'o']
```

There are a few other times when we care about mutable and immutable objects (tuples and bytes objects are immutable, while bytearrays are mutable), but for now, let's consider the matter closed.

## Scope

The *scope* of a variable name is the region of code where the name is valid (https://en.wikipedia.org/wiki/Scope_(computer_science)).

Consider the following:

```python
def func1():
    localvar = 42
    print(localvar)

def func2():
    print(localvar)

func1()
# 42

func2()
# NameError: name 'localvar' is not defined
```

The *scope* of the variable `localvar` is restricted to the function `func`.

## Global

A *global* variable is one whose scope is the entire python script.

```python
name = "prod02"

def check_prod():
    print(name)

check_prod()
# prod02
```

However.  Let's try *changing* the value of `name` inside the function:

```python
name = "prod02"

def check_prod():
    name = "prod05"
    print(name)

check_prod()
# prod05

print(name)
# prod02
```

Evidently, the function `check_prod` has automatically created a local `name` and its value did *not* affect the global one.

If we really *do* want to change the global variable, we need to declare it explicitly:

```python
name = "prod02"

def check_prod():
    global name
    name = "prod05"
    print(name)

check_prod()
# prod05

print(name)
# prod05
```

It is best to state your global variables at the beginning of your function.  This code will throw an error:

```python
name = "prod02"

def check_prod():
    name = "prod05"
    global name

# SyntaxError: name 'name' is assigned to before global declaration
```

Python is confused about whether `name` is local or global.

Here is more code that will throw an error:

```python
name = "prod02"

def check_prod():
    print(name)
    name = "prod05"

check_prod()
# UnboundLocalError: local variable 'name' referenced before assignment
```

Python knows that you intend to use `name` as a variable inside the function.  However, you printed it *before* you assigned it, so python is confused about whether you're referencing the *global* variable `name` or the *local* variable `name`.  In general, it's better to be explicit about these things.

Here's another (often-missed) case that will throw an error:

```python
name = "prod02"

if __name__ == '__main__':
    global name
    print(name)

# SyntaxError: name 'name' is assigned to before global declaration
```

Again the problem is that python doesn't know whether `name` is local or global.  The important thing to point out here is that the `global` keyword in this case is redundant, as the scope of `name` already include the `if` block.  The `if` block is *not* a function, and therefore does not have a separate scope (like other functions).

**Warning**: global variables often allow for quick-fixes... However, *most* of the time, it is probably better to avoid global variables.  If you think you have a problem on your hands which you think can only be solved with a global variable, consider if [classes](../classes) can help you at all.

## Nonlocal

The `nonlocal` keyword is used for similar reasons as the `global` keyword.  If you want to alter a variable in the closest enclosing scope (furthermore, without affecting the global scope).

**Disclaimer**: I have never personally used the `nonlocal` keyword.  I imagine there are probably cases where this is the best solution, but I have not yet found one.

Because of the rarity of this keyword, let's see if we can get away with just an example:

```python
x = 1

def outer():
    x = 2
    def inner():
        x = 3
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
# Inner: 3
# Outer: 2

print("Global:", x)
# Global: 1
```

As you can see, each assignment of `x` is only valid locally.

Let's add `nonlocal` inside the `inner` function:

```python
x = 1

def outer():
    x = 2
    def inner():
        nonlocal x
        x = 3
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
# Inner: 3
# Outer: 3

print("Global:", x)
# Global: 1
```

This time, the `x` inside `inner` was declared to alter the value of `x` from `outer`  (confused yet?).

Last adjustment, let's change `nonlocal` to `global` and see what happens.

```python
x = 1

def outer():
    x = 2
    def inner():
        global x
        x = 3
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
# Inner: 3
# Outer: 2

print("Global:", x)
# Global: 3
```

This time, the `inner` function changed the value of the global variable, but the `outer` function defined its own local variable.




