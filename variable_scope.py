#!/usr/bin/env python

MAX_VALUE = 100  # GLOBAL name

def spam():
    animal = 'wombat'  # LOCAL name
    print("spam(): MAX_VALUE is", MAX_VALUE)


spam()

print("main: MAX_VALUE is", MAX_VALUE)
# print("main: animal is", animal)

def bob():
    name = 'Tootsie'

    def ray():
        print("name:", name)


