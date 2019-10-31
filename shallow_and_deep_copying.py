#!/usr/bin/env python
from copy import deepcopy

a = ['foo', 'bar', ['spam', 'ham']]
b = a  # alias -- no new object is created

a.append('blah')
print(a, id(a))
print(b, id(b))
print(a is b)
print()

# shallow copies of a
c = list(a)
d = a[::]

a.append("baz")

print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
print()

a[2].append("eggs")
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
print()

e = deepcopy(a)  # deep, or recursive, copy

a[2].append("toast")
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
print(e, id(e))
print()
