#!/usr/bin/env python

value = 57

print(globals())

g = globals()

print(g['value'])
print(value)

g['color'] = 'blue'
print(color)

g['bark'] = lambda : print("woof, woof")

bark()


def spam(x):
    animal = 'wombat'
    print(locals())

spam(5)

