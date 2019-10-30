#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

c1 = CardDeck("Fred")

print(c1)

print(c1.dealer)
c1.dealer = "Abigail"
print(c1.dealer)

try:
    c1.dealer = [5, 6.9]
except TypeError as err:
    print(err)
else:
    print(c1.dealer)

c1.spam("ha ha ha")

c1.shuffle()
print(c1.cards)
print()

for i in range(10):
    print(c1.draw())
print()

print(c1.get_ranks())
print()

print(CardDeck.get_ranks())
print()

c2 = CardDeck("Al")
c2.shuffle()
# CardDeck.shuffle(c2)

j1 = JokerDeck("Jim")
j1.shuffle()
for i in range(5):
    print(j1.draw())
print()
print(j1.cards)
print()
j1.shuffle()

print(len(c1), len(c2))
print(len(j1))

# print(CardDeck.__len__(j1))
print(c1)
print(str(c1))
print(c2)
print(j1)

foo = c1 + j1

print(foo)
print(len(foo))
print(foo.draw())
