# Flow

You already know all about `if, else, for, while, try, except` so what else is there to say?

A couple of interesting corner cases.  I'm including them here for future reference.

## `for-else`

The `for-else` block is rare, probably because the word `else` is not great in the context that it's used, and there are other ways to accomplish the same thing that read a bit better.

Regardless, I present the `for-else` block:

```python
L = [2, 3, 5, 7]

for num in L:
    if num == 5:
        print("Found:", num)
        break

else:
    print("Didn't find it...")
```

The `else` block executes if the for loop finishes without breaking.  It's equivalent to setting a boolean flag like this:

```python
L = [2, 3, 5, 7]
found = False

for num in L:
    if num == 5:
        print("Found:", num)
        found = True
        break

if not found:
    print("Didn't find it...")
```

## `while-else`

Similarly, we can use `while` and `else` together.

```python
a = 0
while a < 10:
    if a == 42:
        print("Found:", a)
        break
    a += 1
else:
    print("Didn't find it...")
```

This `while-else` block is equivalent to this:

```python
a = 0
found = False
while a < 10:
    if a == 42:
        print("Found:", a)
        break
    a += 1

if not found:
    print("Didn't find it...")
```

## `try-except-else-finally`

See also [Exceptions](../exceptions)

We already know that `try` attempts to execute some code, and `except` will execute if an exception is thrown.  To extend on this, `else` will execute if an exception is *not* thrown, and `finally` will execute regardless:

```python
try:
    print("Hello world!")
    # raise Exception("Hello world!")
except:
    print("An exception was raised")
else:
    print("An exception was not raised")
finally:
    print("Moving on with our program")
```

Try running this code, then comment out the `print` line and uncomment the `raise` line, then run it again!


    
