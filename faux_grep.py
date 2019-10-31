#!/usr/bin/env python
import re
import fileinput
import argparse

parser = argparse.ArgumentParser(description="Emulate grep")

parser.add_argument('-i', dest="ignore_case", action="store_true",
                    help="ignore case")

parser.add_argument('-n', dest="show_filename", action="store_true",
                    help="print file name")

parser.add_argument('pattern', help="pattern to find (required)")

parser.add_argument('files', help="files to search", nargs="*")

args = parser.parse_args()

# print(args)

pattern  = re.compile(args.pattern, re.I if args.ignore_case else 0)

for line in fileinput.input(args.files):  # open sys.argv[1], sys.argv[2],....
    if pattern.search(line):
        if args.show_filename:
            print(fileinput.filename(), end=' ')
        print(line.rstrip())
