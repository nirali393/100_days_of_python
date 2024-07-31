# -------------------Exercise 1---------------------------- 
# Using the built-in datetime module, the date and timedelta classes from the given date 2020-01-01 00:00:00 get the date:
# shifted by 7 days
# shifted by 30 days
# shifted by 30 hours
# shifted by 15 minutes

# Tip:
# >>> help(datetime.timedelta)
# Help on class timedelta in module datetime:

# class timedelta(builtins.object)
#  |  Difference between two datetime values.
#  |  
#  |  timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#  |  
#  |  All arguments are optional and default to 0.
#  |  Arguments may be integers or floats, and may be positive or negative.
# Expected result:
# 2020-01-08 00:00:00
# 2020-01-31 00:00:00
# 2020-01-02 06:00:00
# 2020-01-01 00:15:00
# ---------------------------------------------------------

import datetime
 
 
dt = datetime.datetime(2020, 1, 1)
 
 
print(dt + datetime.timedelta(days=7))
print(dt + datetime.timedelta(days=30))
print(dt + datetime.timedelta(hours=30))
print(dt + datetime.timedelta(minutes=15))
