# Wrappers

The word *wrapper* is sort of an all-purpose word that describes the following process:

Sometimes you want many functions to have *slightly* different operations but all have a similar template.  Write the unique operations into different **inner** functions, and write the template into an **outer** function which will *extend* the operation of the inner functions.

## Intro

Example
```python
# This function creates wrappers
# Observe that it returns a function!!
def ez_wrapper(inner):
    def wrapper():
        print("This code will always run before")
        inner()
        print("This code will always run after")
    return wrapper

# Here are two inner functions which will be passed to ez_wrapper
def secret():
    print("Here is where secret stuff will happen")

def public():
    print("Here is where public stuff will happen")

# Make wrappers for the secret and public functions
wrapped_secret = ez_wrapper(secret)
wrapped_public = ez_wrapper(public)

wrapped_secret()
# This code will always run before
# Here is where secret stuff will happen
# This code will always run after

wrapped_public()
# This code will always run before
# Here is where public stuff will happen
# This code will always run after

# Compare to this
secret()
# Here is where secret stuff will happen

public()
# Here is where public stuff will happen
```

Now, since `ez_wrapper` returns a function that is intended to be used as an all-purpose wrapper, it shouldn't be necessary to always know exactly the arguments that should be passed (to `wrapper` and therfore to `inner`).

That means it is actually *very* convenient in this case to use `*args` and `**kwargs`.  (In fact, this is standard practice, which we will adopt for all the other wrappers we discuss on this page).

(See section [Args and Kwargs](../basics#args-and-kwargs) for reference).

```python
def better_wrapper(inner):
    def wrapper(*args, **kwargs):
        print("This is the wrapped function")
        return inner(*args, **kwargs)
    return wrapper

def secret(a, b):
    print("My secret numbers are:", a, b)

secret = better_wrapper(secret)

secret(42, 17)
# This is the wrapped function
# My secret numbers are: 42 17
```

A couple of notes about the previous example:
  - I used `return` in the wrapper to return the same value that `inner` would have returned (if it wasn't wrapped).
  - I reassigned `secret` to a wrapped version of itself.  The old `secret` function cannot be recovered afterward.  (And maybe that's a good thing).


## Decorators

Decorators are a type of wrapper that allow for some very nice [*syntactic sugar*](https://en.wikipedia.org/wiki/Syntactic_sugar).

We are going to accomplish the same results as in the last example in the [Wrappers](#wrappers) section, but using the @ notation.

```python
def ez_wrapper(inner):
    def wrapper(*args, **kwargs):
        print("This code will always run before")
        inner(*args, **kwargs)
        print("This code will always run after")
    return wrapper

# This piece of code passes the function "secret" as an argument to ez_wrapper
# The result is the wrapped function
@ez_wrapper
def secret():
    print("Here is where secret stuff will happen")

@ez_wrapper
def public():
    print("Here is where public stuff will happen")

secret()
# This code will always run before
# Here is where secret stuff will happen
# This code will always run after

public()
# This code will always run before
# Here is where public stuff will happen
# This code will always run after
```

This also eliminates the need to call the wrapper function.

### Decorators with arguments

This section needs some explanation.

```python

def shiny(arg):
    def smart_wrapper(inner):
        def wrapper(*args, **kwargs):
            print("Wrapper called with arg:", arg)
            print("This code will always run before")
            inner(*args, **kwargs)
            print("This code will always run after")
        return wrapper
    return smart_wrapper

# This passes "/secret" as an argument to shiny
# The return value from shiny should be a function
# Whatever function is returned, the function "secret" is passed as an argument
# The result is the wrapped function
@shiny("/secret")
def secret():
    print("Secret stuff!")

@shiny("/public")
def public():
    print("Public stuff!")

secret()
# Wrapper called with arg: /secret
# This code will always run before
# Secret stuff!
# This code will always run after

public()
# Wrapper called with arg: /public
# This code will always run before
# Public stuff!
# This code will always run after
```
