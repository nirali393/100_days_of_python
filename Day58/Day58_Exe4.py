# -------------------Exercise 4---------------------------- 
# Using the built-in datetime module, determine the number of days between 2020-07-21 and 2020-12-31.
# Then print the result to the console as shown below.
# Expected result:
# Number of days: 163
# ---------------------------------------------------------

import datetime
 
d1 = datetime.date(2020, 7, 21)
d2 = datetime.date(2020, 12, 31)
diff = (d2 - d1).days
 
print(f'Number of days: {diff}')
