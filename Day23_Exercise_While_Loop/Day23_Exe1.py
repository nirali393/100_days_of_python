# -------------------Exercise 1----------------------------
# Write a program that creates a histogram as a dictionary of the following values:
# items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

# In response print histogram to the console.
# Expected result:
# {'x': 3, 'y': 4, 'z': 2}
# ----------------------------------------------------------

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
temp = {}

for i in items:
    if i not in temp:
        temp[i] = items.count(i)
print(temp)
