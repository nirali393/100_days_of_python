# -------------------Exercise 4-------------------

# Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.
# Tip: Use compound capitalization of interest.

# Print the result to the console as shown below.
# Expected result: The future value of the investment: 1159.27 USD
# --------------------------------------------------


# Compound Interest Formula
# FV = PV × (1+r)^n

pv = 1000
r = 3/100  # rate is 3%, so devide by 100 to convert it to decimal
n = 5

fv = pv* pow(1+r,n)

print(fv)
