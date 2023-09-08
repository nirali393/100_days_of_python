# -------------------Exercise 1-------------------------
# Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.

# Expected result: Geometric average of the given numbers: 4.05
# --------------------------------------------------

a, b, c, d = 4, 3, 4.5, 5

mean = pow(4*3*4.5*5,1/4)
print(f'Geometric average of the given numbers: {mean:.2f}')
