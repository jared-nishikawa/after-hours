# Exceptions

Consider the following code (strictly python3):
```python
num = input("Enter your age: ")

age = int(num)

print("You are", age, "years old.")
```

This script works fine as long the user enters a valid integer.

But inputs like `forty-two` or `foobar` will cause the script to throw an error:

`ValueError: invalid literal for int() with base 10: 'forty-two'`

The `input()` function *always*  returns a `str` (string).  For posterity, python2's `raw_input()` function does this, and the `input()` function does something different.

So, we are trying to cast a string into an integer.  Python will get confused if that string is not obviously an integer.  Strings like `"42"` or `"314"` are perfectly fine, but `"forty-two"` or even `"3.14"` will cause the cast to throw the `ValueError`.

It would be great if we could somehow *catch* this error before it causes the entire script to crash.  To "catch" an error in this context means to establish a safety net of code, where if an error is thrown we have some logic that handles the program's behavior (instead of crashing).

It's sort of like an `if-then` clause for catching errors.

(But it's called `try-except`).

Observe:

```python
num = input("Enter your age: ")

# Isolate the code that could throw the error
try:
    age = int(num)

# Specify the logic for if an error is thrown
except ValueError:
    print("That is not an integer!")
    exit()

print("You are", age, "years old.")
```


