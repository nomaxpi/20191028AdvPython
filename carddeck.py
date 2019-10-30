#!/usr/bin/env python
import random
from typing import Union, Iterable, List

class CardDeck:  # inherits from object
    #  __init__()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'clubs diamonds hearts spades'.split()
    ANIMALS = ['wombat', 'wildebeest', 'moose']

    def __init__(self, dealer: str):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    # instance method
    def shuffle(self):  # self is current instance
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()  # remove 1 card and return it

    @property
    def cards(self):
        return self._cards
    # cards = property(cards)

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, value: str):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    def spam(self, x: Union[int, float]) -> float:
        pass

    def ham(self, thing: List[str]) -> None:
        pass

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    # instance method
    def get_ranks2(self):
        return self.RANKS

    @staticmethod
    def foom():
        pass

    def __len__(self):  # used for len(instance)
        return len(self._cards)

    def __str__(self):  # to_string() method
        my_name = self.__class__.__name__
        return "{}({}, {})".format(my_name, self.dealer, len(self))

    def __add__(self, other): # implements + operator
        temp = self.__class__(self.dealer)
        temp._cards = self.cards + other.cards
        return temp
