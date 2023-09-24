# -------------------Exercise 2----------------------------
# Write a program that checks if the given number is a prime number (use the break statement):
# number = 13

# Print one of the following to the console depends on the result:
# 13 - prime number
# 13 - not a prime number

# Expected result:
# 13 - prime number
# ----------------------------------------------------------
import math

number = 13

for i in range(2, math.isqrt(number)+1):
    if number % i ==0:
        print("Not Prime")
        break
    else: 
        print(f'{number} is a Prime Number')
        break