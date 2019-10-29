#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

empty = ()

singleton = 5,

print(person[0], person[1])

#  list-of-variables = iterable

first_name, last_name, last_name = person

print(first_name, last_name)


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print(type(people))
print(people[0])
print(type(people[0]))
print(people[0][0])
print(type(people[0][0]))
print(people[0][0][0])
print()

for first_name, last_name, *_ in people:
    print(first_name, last_name)

print()


x = ['wombat', 'moose', 'platypus']

for i in range(len(x)):
    print(x[i])
print()

for animal in x:
    print(animal)
print()

data = [('Raleigh', 'NC'), ("Baton Rouge", "LA"),
        ("Boston", "MA"), ("Sacramento", "CA"), ("Lansing", "MI")]

for capital, state in data:
    print(f"{capital} is the capital of {state}")
print()

for i, animal in enumerate(x):
    print(i, animal)
print()

print(list(enumerate(x)), '\n')

# for var, var, .... in iterable:
#      ....





