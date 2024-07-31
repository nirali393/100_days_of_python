# -------------------Exercise 3---------------------------- 
# Using the built-in datetime module calculate the future value of the investment (present value) of USD 1000 with an annual interest rate of 4% (rate) 
# and daily compound capitalization of interest, 
# assuming the duration of the investment from 2021-07-01 to 2021-12-31. For calculations, 
# assume that the year has 365 days.

# Print the future value to the console as shown below.

# Expected result:
# Future value: $ 1020.26
# ---------------------------------------------------------

import datetime
 
 
rate = 0.04
pv = 1000
 
daily_rate = rate / 365.0
d1 = datetime.date(2021, 7, 1)
d2 = datetime.date(2021, 12, 31)
duration = d2 - d1
fv = pv * (1 + daily_rate) ** duration.days
 
 
print(f'Future value: $ {fv:.2f}')