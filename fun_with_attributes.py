#!/usr/bin/env python
from president import President
from trivera.utils import coolstuff

p = President(26)

print(p.first_name, p.last_name)

print(dir(p), '\n')

field_wanted = 'party'

print(getattr(p, field_wanted))

print(hasattr(p, field_wanted))

if hasattr(p, 'write'):
    print("OK")
else:
    print("Need object with write() method")

s = getattr(coolstuff, 'spam')
s()
coolstuff.spam()

def get_full_name(self):
    return "{} {}".format(self.first_name, self.last_name)

setattr(President, "get_full_name", get_full_name)

print(p.get_full_name())
