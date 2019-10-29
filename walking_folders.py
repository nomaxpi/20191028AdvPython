#!/usr/bin/env python
import os
from binascii import crc32
from datetime import datetime

#   find foo -name '*.txt' -size +1M -print

TARGET = "."

for folder, subs, files in os.walk(TARGET):
    if '.git' in subs:
        subs.remove('.git')
    print(folder)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            file_timestamp = datetime.fromtimestamp(os.path.getmtime(file_path))
            with open(file_path, 'rb') as file_in:
                file_contents = file_in.read()
            file_crc = crc32(file_contents)
            print("    {:6d} {} {} {}".format(file_size, file_name, file_crc, file_timestamp))
