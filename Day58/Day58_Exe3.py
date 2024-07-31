# -------------------Exercise 3---------------------------- 
# Using the built-in datetime module, create datetime objects for the given dates:
# Jul 20 2020 11:30:00
# 1990-03-10 12:00:00
# 2021-01-01 00:00:00
# Then print these objects to the console.
# Tip:
# >>> help(datetime.datetime)
# Help on class datetime in module datetime:
# class datetime(date)
#  |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
#  |  
#  |  The year, month and day arguments are required. tzinfo may be None, or an
#  |  instance of a tzinfo subclass. The remaining arguments may be ints.
# Expected result:
# 2020-07-20 11:30:00
# 1990-03-10 12:00:00
# 2021-01-01 00:00:00
# ---------------------------------------------------------

import datetime
 
 
dt1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
dt2 = datetime.datetime(1990, 3, 10, 12, 0, 0)
dt3 = datetime.datetime(2021, 1, 1, 0, 0, 0)
 
 
print(dt1)
print(dt2)
print(dt3)