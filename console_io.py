#!/usr/bin/env python
a = 5
b = "splat"
c = ['a', 'b', 'c']
print(a)
print(b, repr(b))
print(c)
print(a, b, c)
print(a, b, c, sep='//')
print(a, b, c, sep='.')
print(a, b, c, sep=' --> ')
print()
print(a, end="*")
print(b, repr(b), end="*")
print(c)
import time
print("Wait...", end='')
# time.sleep(2)
print("done")

result = 29 / 13
print("result is", result)
print("result is", round(result, 3))
test_run = 4
print("result for test run {} is {:.3f}".format(test_run, result))
print(f"result for test run {test_run} is {result:.3f}")








