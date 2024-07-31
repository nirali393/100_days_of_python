# -------------------Exercise 2---------------------------- 
# Using the built-in datetime module, datetime and timedelta classes, create the given list of dates:
# [
#     datetime.datetime(2020, 1, 1, 0, 0),
#     datetime.datetime(2020, 1, 1, 8, 0),
#     datetime.datetime(2020, 1, 1, 16, 0),
#     datetime.datetime(2020, 1, 2, 0, 0),
#     datetime.datetime(2020, 1, 2, 8, 0),
#     datetime.datetime(2020, 1, 2, 16, 0),
#     datetime.datetime(2020, 1, 3, 0, 0),
#     datetime.datetime(2020, 1, 3, 8, 0),
#     datetime.datetime(2020, 1, 3, 16, 0),
#     datetime.datetime(2020, 1, 4, 0, 0),
#     datetime.datetime(2020, 1, 4, 8, 0),
#     datetime.datetime(2020, 1, 4, 16, 0),
# ]
# and assign to variable dates. Dates start from 2020-01-01 00:00:00, end on 2020-01-04 16:00:00 and differ by 8h. Then print each date to the console.

# Expected result:
# 2020-01-01 00:00:00
# 2020-01-01 08:00:00
# 2020-01-01 16:00:00
# 2020-01-02 00:00:00
# 2020-01-02 08:00:00
# 2020-01-02 16:00:00
# 2020-01-03 00:00:00
# 2020-01-03 08:00:00
# 2020-01-03 16:00:00
# 2020-01-04 00:00:00
# 2020-01-04 08:00:00
# 2020-01-04 16:00:00
# ---------------------------------------------------------

import datetime
 
 
dt = datetime.datetime(2020, 1, 1)
delta = datetime.timedelta(hours=8)
dates = [dt + i * delta for i in range(12)]
 
for date in dates:
    print(date)