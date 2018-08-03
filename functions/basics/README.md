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



