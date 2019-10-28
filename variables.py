#!/usr/bin/env python

actor = "Chris Hemsworth"

x = 5

#  a-z A-Z 0-9 _
# GOOD:
#  abc  abc_def  Abc  foo_bar  _   __  a123
# BAD:
#  $x  123abc  5.9  foo-bar

#  lower_case_words_with_underscores

_ = "wombat"

print(x)
print(actor)
print(x, actor)

a = "Apple"
b = a
print(b)
print(a)
print()
a = 123.456
print(a)
print(b)

j = ['a', 'b', 'c']
k = j
j.append('d')
print("j is", j)
print("k is", k)
m = list(j)
j.append('e')
print("j is", j)
print("m is", m)
j = None
print(j, k)

print(None)

print(type(j), type(actor), type(None))


a = 5
b = a

foo = [1, 2, 3]
bar = foo
blah = foo

a = 10
foo = ['a', 'm']
print(id(a), id(b), id(foo), id(bar))

blah.append("sasquatch")
print(blah)
print(bar)
print(foo)
spam = 12
ham = spam

print(id(spam), id(ham))








