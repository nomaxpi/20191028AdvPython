#!/usr/bin/env python

my_str = "Hello"
my_bytes = b"stuff"
my_list = ['a', 'b', 'c']
my_tuple = 'Bill', 'Gates', 'Microsoft'

print(my_str[0], my_bytes[0], my_list[0], my_tuple[0])

print(len(my_str), len(my_bytes), len(my_list), len(my_tuple))

print(my_str.count('e'))
print(my_bytes.count(b'f'))
print(my_list.count('c'))
print(my_tuple.count('Gates'))
