#!/usr/bin/env python
from collections import Counter

data = 13, 18, 13, 14, 13, 16, 14, 21, 13, 18, 15, 15, 12
data = range(10, 20)

data_len = len(data)

mean = sum(data) / data_len

median_point = (data_len + 1 if data_len % 2 else data_len) // 2

median = sorted(data)[median_point]

if data_len == len(set(data)):
    mode = None
else:
    c = Counter(data)
    mode = c.most_common(1)[0][0]

range = max(data) - min(data)

print(mean, median, mode, range)
