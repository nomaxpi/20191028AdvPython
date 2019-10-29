#!/usr/bin/env python
import calendar

tcal = calendar.TextCalendar()  # <1>
cal = tcal.formatmonth(2012, 1)
print(cal)  # <2>

print()
