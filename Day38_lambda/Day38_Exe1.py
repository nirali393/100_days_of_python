# -------------------Exercise 1----------------------------
# The following list is given:
# items = [(3, 4), (2, 5), (1, 4), (6, 1)]

# Sort the list by the growing sum of squares of numbers in each tuple. Use the sort() method and the lambda expression and print sorted list to the console.

# Expected result:

# [(1, 4), (3, 4), (2, 5), (6, 1)]
# ---------------------------------------------------------

items = [(3, 4), (2, 5), (1, 4), (6, 1)]
items.sort(key=lambda item: item[0]**2 + item[1]**2)
print(items)
    