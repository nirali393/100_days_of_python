# -------------------Exercise 2----------------------------
# Write a program that checks if the given item:

# item = '001'
# is in the list:
# items = ['001', '000', '003', '005', '006']

# If so, remove this item from the list and print this list to the console.

# Expected result:
# ['000', '003', '005', '006']
# ---------------------------------------------------------

item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)
    print(items)
else:
    print(f'{item} is not present')