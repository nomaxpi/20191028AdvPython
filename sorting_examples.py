#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

data = [('Raleigh', 'NC'), ("Baton Rouge", "LA"),
        ("Boston", "MA"), ("Sacramento", "CA"), ("Lansing", "MI")]

f0 = sorted(fruits)
print("f0:", f0, '\n')

n0 = sorted(nums)
print("n0:", n0, '\n')

d0 = sorted(data)
print("d0:", d0, '\n')

def ignore_case(fruit):
    return fruit.lower()

f1 = sorted(fruits, key=ignore_case)
print("f1:", f1, '\n')

def by_state(e):
    print("e:", e)
    return e[1]

d1 = sorted(data, key=by_state)
print("d1:", d1, '\n')

def david_sort(item):
    return len(item), item.lower()

f2 = sorted(fruits, key=david_sort)
print("f2:", f2, '\n')

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

def by_dob(e):
    return e[3]

for first_name, last_name, product, dob in sorted(people, key=by_dob):
    print(first_name, last_name, dob)
print('-' * 60)

for first_name, last_name, product, dob in sorted(people, key=lambda e: (e[1], e[0])):
    print(first_name, last_name, dob)
print('-' * 60)

def some_name(e):
    return e[1], e[0]

add = lambda a, b: a + b  # NOT best practice
print(add(10, 15))

