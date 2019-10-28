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

