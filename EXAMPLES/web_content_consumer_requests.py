#!/usr/bin/env python
from pprint import pprint
import sys
import requests


BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>


def main(args):
    if len(args) < 1:
        print("Please specify at least one search term")
        sys.exit(1)

    for term in args:
        response = requests.get(
            BASE_URL + term,
            params={'key': API_KEY},
        )  # <3>

        if response.status_code == requests.codes.OK:
            # pprint(response.content.decode())
            # print('-' * 60)
            data = response.json()  # <4>
            for entry in data: # <5>
                if isinstance(entry, dict):
                    meta = entry.get("meta")
                    if meta:
                        part_of_speech = '({})'.format(entry.get('fl'))
                        word_id = meta.get("id")
                        print("{} {}".format(word_id.upper(), part_of_speech))
                    if "shortdef" in entry:
                        print('\n'.join(entry['shortdef']))
                    print()
                else:
                    print(entry)
            print('=' * 20)
        else:
            print("Sorry, HTTP response", response.status_code)


if __name__ == '__main__':
    main(sys.argv[1:])
