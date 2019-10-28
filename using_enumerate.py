#!/usr/bin/env python

colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)

for i, color in enumerate(colors, 1):
    print(i, color)
print('-' * 60)

i = 0
for color in colors:
    print(i, color)
    i += 1
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print()

for i in range(10, 20):
    print(i, end=',')
print('\n')



