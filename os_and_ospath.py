#!/usr/bin/env python
import os

print(os.getcwd())
print(os.getpid())
print(os.getppid())
print(os.getuid())
print(os.getlogin())

print(os.listdir('DATA'))
print()

for node in os.scandir('DATA'):
    if node.is_file():
        print(node.name)
print()

# os.rmdir('DELETE_ME')
# os.mkdir('DELETE_ME')
print(os.listdir('.'))

# os.makedirs('spam/ham/eggs/toast')

os.remove('DATA/mary.txt')
print(os.listdir('DATA'))
