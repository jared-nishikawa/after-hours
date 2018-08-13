# Modules

Part of what makes python so great is its vast quantity of *modules*.

A module is made up of classes, functions, and constants that are not available until you *import* the module.

```python
print(math.pi)
# NameError: 'math' is not defined

import math
print(math.pi)
# 3.141592653589793
```

Python comes equipped with the [Python Standard Library](https://docs.python.org/3/library/), which is a set of modules that will be available in all implementations of python.  This provides a nice guarantee of functionality: if I give you a script that contains only modules from the Python Standard Library, I can be (more or less) assured that it will run on your system.

Other modules have to be downloaded and installed to your system before you can import them.

## Imports

There are many ways to import modules into your script.

The simplest and most common way is like this:

```python
import math
print(math.pi)
# 3.141592653589793
```

Some modules have long names, and it becomes cumbersome to type `somemodule.func` over and over, so it is often convenient to state the import using a different name:

```python
import math as mt
print(mt.pi)
# 3.141592653589793
```

For even more brevity, you may want to eliminate the need to type `somemodule.` at all, and import the function or constant directly.  In that case, there is a slightly different syntax:

```python
from math import pi
print(pi)
# 3.141592653589793
```

You can even combine both syntaxes:

```python
from math import pi as PI
print(PI)
# 3.141592653589793
```

One reason you might consider doing this is if two modules have a function named `connect` (for example).  You could import like this:

```python
import mod1
import mod2

mod1.connect()
mod2.connect()
```

But if you wanted to import the functions directly, this would cause problems:

```python
from mod1 import connect
from mod2 import connect
```

This will cause the second import to overwrite the first (because the functions have the same name).

We can import the functions by assigning unique names, however:

```python
from mod1 import connect as connect1
from mod2 import connect as connect2
```

At this point, one wonders if it might be more clear to simply import the modules and use the dot nomenclature (as in the first example).

Because of these variable name collisions, you want to exercise caution when using this last method for importing:

```python
from math import *
print(pi)
# 3.141592653589793
```

This will import all the functions/classes/constants directly into your script, which could cause collisions with other imports or variable names.

Use restraint with these sorts of imports.  It's usually clearer to simply use the `import math` syntax.

## Making a module

We are going to make a very simple module, with a function and a variable.

Start by opening a new text file (using `vim` or your second favorite text editor).  Call the file whatever you like, but make sure it ends in `.py`.  I'll call this one `foo.py`.  Just make sure you only use alphanumeric characters and underscores.

```python
# foo.py
def hello():
    print("Hello world!")

life = 42
```

Now, open *another* text file (I'm calling this one `main.py`), and enter this:
```python
# main.py
import foo
foo.hello()
print(foo.life)
```

Save, and run with `python main.py`.  You should see output like this:

```python
Hello world!
42
```

Awesome, right!?
    

## `__name__` and `__main__`

Many people have seen this statement (and use it themselves!) but are unsure what it is for:
```
if __name__ == '__main__':
```

Its purpose is best explained with an example.

### Example 1

In a new text file `foo.py` enter the following:

```python
# foo.py
def hello():
    print("Hello world!")

life = 42

print("This is a test of the foo module.  I'd like to make sure it works")
hello()
print(life)
```

Now, if you run this file using `python foo.py` you should see output similar to this:

```
This is a test of the foo module.  I'd like to make sure it works
Hello world!
42
```

Excellent.  Everything is working as expected.

Now try this.  Open a text file `main.py` and enter the following:

```python
# main.py
import foo

print("*******")
print("I have now imported the foo module")
foo.hello()
print(foo.life)
```

Run this file with `python main.py`.  You should see output similar to this:

```
This is a test of the foo module.  I'd like to make sure it works
Hello world!
42
*******
I have now imported the foo module
Hello world!
42
```

What has happened is this: when we imported the foo module, it automatically ran everything inside the script.

It would be great if we could have some sort of distinction between a script that has been called directly, and one that is being imported as a module.  To that end, we will add one line to `foo.py`.

### Example 2
`foo.py` should look like this:

```python
# foo.py
def hello():
    print("Hello world!")

life = 42

print("This is a test of the foo module.  I'd like to make sure it works")
hello()
print(life)
print("My name is:", __name__)
```

Now, if you run this file using `python foo.py` you should see output similar to this:

```
This is a test of the foo module.  I'd like to make sure it works
Hello world!
42
My name is: __main__
```

But now... run `python main.py` again and the `__name__` variable will change:

```
This is a test of the foo module.  I'd like to make sure it works
Hello world!
42
My name is: foo
*******
I have now imported the foo module
Hello world!
42
```

It turns out that when a script is called directly, the builtin `__name__` variable is set to `__main__` and when it is imported, `__name__` is set to the name of the module.

Conclusion: if you want some code to only run when a script is called directly (and not when it is imported as a module), check to see if `__name__` is `__main__`.

### Example 3

```python
# foo.py
def hello():
    print("Hello world!")

life = 42

if __name__ == '__main__':
    print("This is a test of the foo module.  I'd like to make sure it works")
    hello()
    print(life)
```

