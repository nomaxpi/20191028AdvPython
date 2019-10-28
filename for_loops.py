#!/usr/bin/env python


# for VAR ... in ITERABLE:
#    VAR = next(ITERABLE)
#    do something with VAR

for i in range(5):
    print(i)
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for fruit in fruits:
    if fruit[0] == 'a':
        continue
    if fruit[0] == 't':
        break
    print(fruit[:3].upper())
print()

target = 'p'
for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print(f"fruit starting with '{target}' Not found!")
