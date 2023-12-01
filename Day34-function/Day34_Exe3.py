# -------------------Exercise 3----------------------------
# Implement a function called factorial() that calculates the factorial for a given number.

# Example:

# [IN]: factorial(6)
# [OUT]: 720


# [IN]: factorial(10)
# [OUT]: 3628800
# ---------------------------------------------------------
import math

num = int(input("Enter a number: "))
def factorial():
    result = math.factorial(num)
    print(result)

factorial()
