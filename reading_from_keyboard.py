#!/usr/bin/env python
from getpass import getpass

user_name = input("What is your name? ")
print("Hello,", user_name)

user_password = getpass("What is your password? ")
print("password is:", user_password)
