#!/usr/bin/env python
def bark(self):
    print("Woof! woof!")

def wag_tail(self):
    print("wag wag wag wag")

Dog = type('Dog', (), {'bark': bark, 'wag': wag_tail, 'color': 'blue'})

fido = Dog()

fido.bark()
fido.wag()
print(Dog.color)



