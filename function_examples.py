#!/usr/bin/env python

def spam():
    return 'ham'

eggs = spam()
print("eggs:", eggs, '\n')

def dull():
    pass

dull()

def get_message():
    return "Hello, virtual Python world"

m = get_message()
print(m)

def print_message():
    m = get_message()
    print(m)


print_message()


# def FUNCTION_NAME(param1, param2, ....):
#     code
#     code
#     code
#
#     return VALUE


def addem(a, b):
    return a + b

print(addem(5, 6))


def average(*nums):
    return sum(nums) / len(nums)


print(average(5, 18, -2, 6))

def greet(greeting, *whom):
    for who in whom:
        print("{}, {}".format(greeting, who))
    print()


greet("Howdy", 'partner', 'Mom', 'Uncle Herbie')

def parse_log(*, infile, dest):
    print("file_name:", infile)
    print("destination_folder:", dest)
    print()

parse_log(infile='foo.txt', dest='/tmp')

def config(**values):
    for k, v in values.items():
        print(k, v)
    print()

config(animal='wombat', country='Brazil', firearm="Winchester rifle")

def wacky(p1, p2=100, *p3, p4, p5="airbag", **p6):
    pass


wacky('a', 'b', p4='c', p5='d')

wacky('a', 'b', 'c', 'd', 'e', p5="f", p4="g", h=5, j=10, k=99)

wacky('spam', p4="foo", p5="bar")

wacky('spam', p4="foo")













