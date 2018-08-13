# Classes

The unfortunate thing about classes is that they are hard to explain unless there is some code handy that would greatly benefit from using them.  And any code that *would* benefit from classes is not usually good as an introduction to classes.

## Intro

Futile though it might be, here's my attempt to explain classes with a simple example.

```python
# Pretend this is some testing code
# (it doesn't work, so don't bother typing it, but try to understand the spirit behind it).

def connect():
    prod = "prod05"
    send_connection_request(prod)
    authenticate()

def orgs():
    prod = "prod05"
    orgs = get_orgs(prod)
    return orgs

def alerts():
    prod = "prod05"
    org = 3434
    alerts = get_alerts(prod, org)
    print(alerts)
```

Hopefully as you're looking at this code, you've caught on to how annoying it is to type `prod = "prod05"` over and over.  It's messy, inefficient, and not pythonic.

Let's try again:

```python
prod = "prod05"

def connect():
    send_connection_request(prod)
    authenticate()

def orgs():
    orgs = get_orgs(prod)
    return orgs

def alerts():
    org = 3434
    alerts = get_alerts(prod, org)
    print(alerts)
```

Ok... but hang on.  Someone once told me to try to avoid using global variables.  Furthermore, what if I want to change `prod` later to something besides `"prod05"`?  Maybe we should just pass in `prod` as a parameter to all these functions.
```python
def connect(prod):
    send_connection_request(prod)
    authenticate()

def orgs(prod):
    orgs = get_orgs(prod)
    return orgs

def alerts(prod):
    org = 3434
    alerts = get_alerts(prod, org)
    print(alerts)

p2 = "prod02"
connect(p2)
orgs(p2)
alerts(p2)

p5 = "prod05"
connect(p5)
orgs(p5)
alerts(p5)
```

Well, it's not perfect, but at least I've avoided global variables.  Pretty annoying how I have to keep sending in the same parameter over and over.

What I would *like* is some sort of "sub-global" variable... a variable that exists within a fairly large scope (i.e., among several different functions), but *not* in the entire program.

We can solve this particular problem with **classes**.
```python
class Prod():
    def initialize(self, prod):
        self.prod = prod
    
    def display(self):
        print("My prod is:", self.prod)

    def connect(self):
        send_connection_request(self.prod)
        authenticate()
    
    def orgs(self):
        orgs = get_orgs(self.prod)
        return orgs
    
    def alerts(self):
        org = 3434
        alerts = get_alerts(self.prod, org)
        print(alerts)

p2 = Prod()
p2.initialize("prod02")
p2.connect()
p2.orgs()
p2.alerts()

p5 = Prod()
p5.initialize("prod05")
p5.connect()
p5.orgs()
p5.alerts()
```

What this class does is establish a template.  Each *instance* of this template creates its own context for variables and functions.

It's important to keep in mind the distinction: a *class* is an abstract template, while an *instance* of the class is an object.

### Attributes

A class can have *attributes*, which are variables that are bound to that class.

```python
class Prod():
    company_name = 'carbon black'

P = Prod()
print(P.company_name)
# carbon black
```

You can access these attributes using the dot nomenclature `class.attribute`.

## Methods

The words "method" and "function" are used more or less interchangeably, so I don't really know why the word "method" is more common when talking about functions within classes.

### Instance methods

An *instance method* is a method that when called, must be provided an instance of a class.

Because of this, you *must* always pass `self` as a parameter when defining a new instance method.  The `self` parameter is actually the instance itself (yes, it passes itself to its own function).  Other programming languages do this implicitly (`this` in Java), but it is considered Pythonic to be explicit about it.

The instance method is called using the dot notation `instance.method` and you don't need to specify the instance of the class as the first argument.  It is assumed.

```python
class Prod():
    def hello(self):
        print("Hello world")

    def set_prod(self, prod_name):
        self.prod = prod_name

p = Prod()

# Notice how it takes no arguments here:
p.hello()
# Hello world

# Notice how we pass one argument here:
p.set_prod("prod02")

print(p.prod)
# prod02
```

When `self` is  passed to `set_prod`, we use it to set the `prod` attribute for this instance of the class.

Finally, we should discuss the `__init__` instance method.  It is not required, but it is *always* called whenever a new instance is created.  (Let's forget for the time being how it could possibly be called if you haven't written it!)

```python
class Prod():
    def __init__(self, prod):
        self.prod = prod

    def display(self):
        print(self.prod)

# __init__ gets called here
p = Prod("prod02")

p.display()
# prod02
```

The `__init__` method is called when a new instance of a class is created.  It's useful for *initializing* attributes of the instance or calling other functions that need to be called upon the creation of this new object.

### Static methods

A *static method* is a method associated with a class that isn't associated with (or *bound to*) any particular instance of that class.  As such, it does not require the `self` parameter:

```python
class Prod():
    def display(self):
        print("This is an instance method.")
        print("It requires the self parameter.")

    @staticmethod
    def hello():
        print("This is a static method.")
        print("It does NOT require the self parameter.")
```

Notice also that we used the `@staticmethod` decorator to wrap the `hello` method.  See [the section on decorators](../functions/wrappers#decorators) for more info.

We can call `hello` without an instance of the `Prod` class:
```python
Prod.hello()
# This is a static method.
# It does NOT require the self parameter.
```

Static methods are useful when you have a function that should clearly be associated with or bundled with a particular class, but does not require a specific instance of that class in order to operate.

### Class methods

An *class method* is a method that when called, must be provided a class.

Because of this, you *must* always pass `cls` as a parameter when defining a new class method.  The `cls` parameter is actually the class itself.

The class method is called using the dot notation `class.method` and you don't need to specify the as the first argument.  It is assumed.

Class methods are handy for when you want to change attributes across all instances of a class.

```python
class Prod():
    company_name = "carbon black"

    @classmethod
    def change(cls, new_name):
        cls.company_name = new_name

A = Prod()
B = Prod()

print(A.company_name)
# carbon black

print(B.company_name)
# carbon black

Prod.change("acme")

print(A.company_name)
# acme

print(B.company_name)
# acme
```

Again, notice the use of [decorators](../functions/wrappers#decorators).

Both `staticmethod` and `classmethod` are builtins to be used as decorators.

## Dummy classes trick

There have been a few times in my life where I needed a class for a very singular purpose: it needed attributes.  For whatever reason, a dictionary would not cut it.

Basically, I needed this:

```python
class Dummy():
    def __init__(self):
        self.attr1 = 42
        self.attr2 = 17

D = Dummy()
print(D.attr1)
# 42

print(D.attr2)
# 17
```

I remember spending some time being annoyed that I needed to create an entire class for this, so I went poking around the internet and discovered a shortcut.  The key to this shortcut is the observation that you *can't* set arbitrary attributes for objects like ints, lists, or strings... but you *can* set arbitrary atrtibutes for *functions*.

Observe:

```python
def func():
    return 0

func.attr = 42

print(func.attr)
# 42
```

This is slightly better, but still kind of annoying because of the verbose creation of the function.

Once again, lambdas save the day!

```python
L = lambda: None
L.attr1 = 42
L.attr2 = 17
print(L.attr1)
# 42

print(L.attr2)
# 17
```

I have found this one-liner solution to be useful on more than one occasion (but less than ten), and I find it an amusing solution at that, so I thought it worth sharing.


## Inheritance

We could spend all day talking about inheritance, but we won't.  In fact, we'll keep it to a minimum.

This is where the conversations about classes start to become ridiculous, because the classes are made-up and don't make any sense, from the point of view of practical programming.

```python
class Animal():
    limbs = 4

class Lion(Animal):
    nocturnal = False

class Raccoon(Animal):
    nocturnal = True

L = Lion()
print(L.limbs)
# 4

print(L.nocturnal)
# False

R = Raccoon()
print(R.limbs)
# 4

print(R.nocturnal)
# True
```

We have defined `Lion` and `Raccoon` to be *subclasses* of the `Animal` class.  Both subclasses *inherit* all the functions and attributes of the parent class.

