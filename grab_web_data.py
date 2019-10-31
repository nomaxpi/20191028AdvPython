#!/usr/bin/env python
import requests


response = requests.get('https://www.python.org')

if response.status_code == requests.codes.OK:
    print(response.content.decode())
print('-' * 60)
