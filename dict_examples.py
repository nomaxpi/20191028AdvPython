#!/usr/bin/env python

d1 = dict()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'YYC': 'Calgary',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

print(airports['IAD'], '\n')

for abbr in 'OAK', 'YYC', 'LAX':
    print(abbr, airports.get(abbr, "NOT FOUND"))

print(airports.get('YOW'))

print("BEFORE:")
print(airports)
more_airports = {'YYC': 'Calgary, AB',
        'YOW': "Ottawa", "YYZ": "Toronto"}

airports.update(more_airports)
print("AFTER:")
print(airports)

del airports['SMF']

for abbr, airport in airports.items():
    print(abbr, airport)


foods = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'eggs', 'eggs', 'eggs', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'haggis', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

for f in set(foods):
    print(f, foods.count(f))
print()

food_counts = {}
for food in foods:
    if food not in food_counts:
        food_counts[food] = 0
    food_counts[food] += 1

print(food_counts)

from collections import Counter

c = Counter(foods)
print(c)
print(c.most_common(2))

letters = []
with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]
        letters.append(first_letter)

print(len(letters), letters[:100])

c = Counter(letters)
print(c.most_common(10))
