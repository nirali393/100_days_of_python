# -------------------Exercise 1---------------------------- 
# Using the datetime built-in module, calculate the difference for dates (date 2 - date 1):
# date 1: 2020-06-01
# date 2: 2020-07-18

# Print the result to the console as shown below.
# Expected result:
# 47 days, 0:00:00
# ---------------------------------------------------------
import datetime
x = datetime.datetime.now()
y = datetime.datetime(1998, 8, 30)     
print(f"I exist on earth from {x-y}")