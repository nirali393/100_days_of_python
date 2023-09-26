# -------------------Exercise 1----------------------------
# Two variables defined below are given:

# sum = 3000
# counter = 0

# We want to divide the variable sum by the counter variable. Using the try... except... clause handle the ZeroDivisionError. If the division is done correctly, print the result to the console, otherwise print to the console the following message:
# 'Division by zero.'
# ----------------------------------------------------------

sum = 3000
counter = 0

try:
    result = sum/counter
    print(result)
except ZeroDivisionError:
    print("Divisible by Counter")
