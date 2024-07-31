# -------------------Exercise 1---------------------------- 
# Using the built-in datetime module, the datetime class and the datetime.datetime.strftime() method format the following date:
# 2021-04-20 11:30:00

# To the following formats:
# 2021-04-20
# 20-04-2021
# 04-2021
# April-2021
# 20 April, 2021
# 2021-04-20 11:30:00
# 04/20/21 11:30:00
# 20(Tue) April 2021
# Then print the formatted dates to the console.

# Tip:
# >>> help(datetime.datetime.strftime)

# Help on method_descriptor:
# strftime(...)
# format -> strftime() style string.

# Expected result:
# 2021-04-20
# 20-04-2021
# 04-2021
# April-2021
# 20 April, 2021
# 2021-04-20 11:30:00
# 04/20/21 11:30:00
# 20(Tue) April 2021
# ---------------------------------------------------------

from datetime import datetime
 
 
dt1 = datetime(2021, 4, 20, 11, 30, 00)
 
 
print(dt1.strftime('%Y-%m-%d'))
print(dt1.strftime('%d-%m-%Y'))
print(dt1.strftime('%m-%Y'))
print(dt1.strftime('%B-%Y'))
print(dt1.strftime('%d %B, %Y'))
print(dt1.strftime('%Y-%m-%d %H:%M:%S'))
print(dt1.strftime('%m/%d/%y %H:%M:%S'))
print(dt1.strftime('%d(%a) %B %Y'))