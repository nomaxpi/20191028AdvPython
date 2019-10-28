#!/usr/bin/env python

list1 = list()

list2 = ['a', 'b', 'c']

list3 = []

words = "wombat weasel joey".split()

print(list2[0])
print(words[1])

words.append("platypus")
print(words)
words.insert(0, "cane toad")
print(words)
words.insert(2, "marmot")
print(words)
more_words = ['honey badger', 'pine martin', 'coatimundi']

words.extend(more_words)
print(words)

del words[0]
print(words)

x = words.pop()
print(x)
print(words)

x = words.pop(2)
print(x)
print(words)

words.remove('platypus')
print(words)

target = 'moose'
if target in words:
    words.remove(target)

for word in words:
    print(word)
print()

print(words[-1])
print(words[-2])

try:
    words.remove('moose')
except ValueError as err:
    print(err)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[:3])
print(fruits[2:6])
print(fruits[-5:])
print(fruits[-5:len(fruits)])

person = "Joe Schmoe"
print(person[:3])
print(person[-6:])

for fruit in fruits:
    print(fruit.upper())
print()

for char in person:
    print(char)
print()


# SEQ[START:STOP]  SEQ[START:STOP:STEP]
# SEQ[:STOP]  SEQ[START:]

x = "gumball giraffe garage griffin"
print(x[::2])
print(x[1::2])

print(fruits)

more_fruits = ['boysenberry', "jack fruit", "durian"]

fruits[1:3] = more_fruits

print(fruits)

fruits[9:12] = []

print(fruits)
