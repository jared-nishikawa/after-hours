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

Ok... but hang on.  Someone once told me to try to avoid using global variables.  Maybe we should just pass in `prod` as a parameter to all these functions.
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

## Methods

Methods and functions are used more or less interchangeably, so I don't really know why the word "method" is ore common when talking about functions within classes.

### Instance methods

An *instance method* is a function that can only be called when by an instance of the abstract class.

You *must* always pass `self` as a parameter in an instance method.  The `self` parameter is actually the instance itself (yes, it passes itself to its own function).  Other programming languages do this implicitly (`this` in Java), but it is considered Pythonic to be explicity about it.

```python
class Prod():
    def hello(self):
        print("Hello world")

    def set_prod(self, prod):
        self.prod = prod

p = Prod()

# Notice how it takes no arguments here:
p.hello()
# Hello world

# Notice how we pass one argument here:
p.set_prod("prod02")

print(p.prod)
# prod02
```

It is worth reflecting on this example and thinking about how `self` works as well as the period (".") nomenclature.

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

### Static methods

### Class methods


## Inheritance
