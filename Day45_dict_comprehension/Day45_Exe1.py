# -------------------Exercise 1---------------------------- 
# The following dictionary is given:
#     data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
# Convert this dictionary into the following list and print the result to the console.

# Expected result:
#     [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6]]
# ---------------------------------------------------------

data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))

new_list = [[k, data[k]] for k in data.keys()]
print(new_list)
