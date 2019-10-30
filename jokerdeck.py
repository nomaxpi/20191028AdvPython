#!/usr/bin/env python
from carddeck import CardDeck

class Thing:
    def shuffle(self):
        print("every day I'm shuffling")

class JokerDeck(Thing, CardDeck):

    def _make_deck(self):
        super()._make_deck()
        j1 = ('1', 'Joker')
        j2 = ('2', 'Joker')
        self._cards.append(j1)
        self._cards.append(j2)

