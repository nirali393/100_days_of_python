# -------------------Exercise 3----------------------------
# Two lists are given:
# num1 = [4, 2, 6, 2, 11]
# num2 = [5, 2, 3, 3, 9]

# Using the map() function and lambda expression, create a list containing the remainders of dividing the first list by the second (elementwise).

# Expected result: [4, 0, 0, 2, 2]
# ---------------------------------------------------------

num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

print(list(map(lambda x, y: x % y, num1, num2)))
