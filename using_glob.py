#!/usr/bin/env python
from glob import glob

text_files = glob('DATA/*.txt')

print(text_files, '\n')

python_scripts = glob('*.py')
print(python_scripts, '\n')

print(glob("wombat.*"))

