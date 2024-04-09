# -------------------Exercise 1---------------------------- 
# The following list is given:

# items = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Implement a function called flatten(), which takes the nested list and returns the following:

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Note: You only need to implement this function.
# ---------------------------------------------------------

items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def flatten(items):
    sub_items = []
    for i in items:
        sub_items.extend(i)
    print(sub_items)
        
flatten(items)
