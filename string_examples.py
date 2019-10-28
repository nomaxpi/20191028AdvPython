#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

print("Guido's the man")
print('Guido is the "man"')
print('''Guido's the "man"''')

query = """
select cost, profit, fudge_factor
from customer_data
where date > '2019-07-01'
"""
print(query, '\n')

print(repr(query), '\n')

actor = "Chris Hemsworth"

print(actor.upper(), actor.lower())

print(actor.count('h'))
print(actor.find('H'))
print(actor.find('worth'))
print(actor.count('H'))
print(actor.lower().count('h'))

s = "     All my exes live in Texas     "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print(s.replace(' ', ''))
print(s.replace('Texas', 'Louisiana'))
print()

s = "xxyyyyxxyyxAll my exes live in Texasyxyxyxyyy"
print("|" + s.lstrip('xy') + "|")
print("|" + s.rstrip('xy') + "|")
print("|" + s.strip('xy') + "|")
print()
