#!/usr/bin/env python

while True:
    user_name = input("Enter user name (or q to quit): ")
    if user_name == '':
        continue
    elif user_name == 'q':
        break
    else:
        print("processing {}...".format(user_name))
print()

i = 0
while i < 5:
    print(i)
    i += 1
