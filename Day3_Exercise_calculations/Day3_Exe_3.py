# -------------------Exercise 3-------------------
# Find the roots of the quadratic equation: x^2 + 5x + 4 =0

# Print the result to the console as shown below.
# Expected result: 
# x1 = -4.0
# x2 = -1.0
# --------------------------------------------------
from math import sqrt
a = 1
b = 5
c = 4

# quadratic formula: x = (-b ± √ (b^2 - 4ac)) / (2a)
x1 = (-b - sqrt(pow(b,2)- 4*a*c))/2*a
x2 = (-b + sqrt(pow(b,2)- 4*a*c))/2*a


print(f'x1 = {x1}')
print(f'x2 = {x2}')
