#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

mary_in = open('DATA/mary.txt')
#  process file
mary_in.close()

with open('DATA/mary.txt', 'r') as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents))
    print("cooked:")
    print(contents)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    all_lines_without_nl = contents.splitlines()
    print(all_lines_without_nl)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitdata.txt', 'w') as fruitdata_out:
    for fruit in fruits:
        fruitdata_out.write(fruit + '\n')

