#!/usr/bin/env python
from trivera.utils.coolstuff import spam, ham

spam()
ham()


def foo():
    from trivera.utils import coolstuff
    coolstuff._eggs

for i in range(10):
    foo()


