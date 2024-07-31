# -------------------Exercise 1---------------------------- 
# Using the built-in datetime module, create date objects for the given dates:
# 2021-01-01
# 31/7/21
# May 7, 1990
# Then print these objects to the console.
# Tip:
# >>> help(datetime.date) 
# Help on class date in module datetime:
# class date(builtins.object)
#  |  date(year, month, day) --> date object
# Expected result:
# 2021-01-01
# 2021-07-31
# 1990-05-07
# ---------------------------------------------------------

import datetime
 
 
d1 = datetime.date(2021, 1, 1)
d2 = datetime.date(2021, 7, 31)
d3 = datetime.date(1990, 5, 7)
 
 
print(d1)
print(d2)
print(d3)