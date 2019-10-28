#!/usr/bin/env python

persons1 = ['Mary', 'Bob', 'Anne', 'Arthur', 'Bill']

persons2 = ['Bob', 'Anne', 'Melinda', 'Max',
            'Bill', 'Rodney', 'Bill', 'Bill', 'Bill']

p1 = set(persons1)
p2 = set(persons2)
p1.add('Robert')
print("p1:", p1)
print("p2:", p2)

values = ['a', 'a', 'a', 'b', 'a', 'c', 'c', 'c','b','a']

s = set(values)
print(s)

print("both:", p1 & p2)
print("just one:", p1 ^ p2)
print("all:", p1 | p2)
print("just p1:", p1 - p2)
print("just p2:", p2 - p1)
