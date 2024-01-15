# -------------------Exercise 2----------------------------
# The following list is given: items = ['P-1', 'R-2', 'D-4', 'F-6']

# Using the map() function and the lambda expression, get rid of the '-' (dash) from each element and print items list on the console.

# Expected result: ['P1', 'R2', 'D4', 'F6']
# ---------------------------------------------------------

items = ['P-1', 'R-2', 'D-4', 'F-6']

print(list(map(lambda item: item.replace('-',''), items)))