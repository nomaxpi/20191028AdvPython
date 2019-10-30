#!/usr/bin/env python
from datetime import datetime
from functools import wraps

class Foo:
    @property
    def bar(self):
        return 42

#  bar = property(bar)

f = Foo()
print(f.bar)


def trivial_deco(wrapped_function):

    @wraps(wrapped_function)
    def replacement_function(*args, **kwargs):
        print(datetime.now().ctime())
        result = wrapped_function(*args, **kwargs)
        return result

    return replacement_function


@trivial_deco
def wombat():
    print("in wombat()!")
    return 1234

# wombat = trivial_deco(wombat)

x = wombat()
print(x)

@trivial_deco
def spam():
    pass

print(spam.__name__)
print(wombat.__name__)

