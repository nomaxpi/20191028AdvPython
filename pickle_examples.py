#!/usr/bin/env python
import pickle

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

with open('airports.pic', 'wb') as airports_out:
    pickle.dump(airports, airports_out)

with open('airports.pic', 'rb') as airports_in:
    a = pickle.load(airports_in)

print(a)

wombat = pickle.dumps(airports)

# now add wombat to S3

print(pickle.loads(wombat))
