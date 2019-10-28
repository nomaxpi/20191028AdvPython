#!/usr/bin/python

with open("../DATA/presidents.txt") as pres_in:
    count_of = {}

    for rec in pres_in:
        fields = rec.split(":")
        state = fields[6]
        if state in count_of:
            count_of[state] += 1
        else:
            count_of[state] = 1

for state, count in sorted(count_of.items()):
    print("%-16s %2d" % (state, count))
