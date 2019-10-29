#!/usr/bin/env python
import os
from datetime import datetime
from humanize import naturalsize

FOLDER = "DATA"
FILENAME = "alice.txt"

file_path = os.path.join(FOLDER, FILENAME)
print("file path:", file_path)

# with open('./pastable.py') as pastable_in:
#     pass

file_size = os.path.getsize(file_path)
print("file size:", file_size)
print("file size:", naturalsize(file_size))
print("is it a file? ", os.path.isfile(file_path))
print("is it a folder? ", os.path.isdir(file_path))
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)
print()

for name in 'fruity.txt', 'DATA/fruity.txt', 'wombats.txt', 'DATA':
    print(name, os.path.exists(name))

print("folder:", os.path.dirname(file_path))
print("file:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))
