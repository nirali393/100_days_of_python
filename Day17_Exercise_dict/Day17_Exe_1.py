# -------------------Exercise 1----------------------------
# The following dictionary is given:
# project_ids = {
#     '01': 'open', 
#     '03': 'in progress',
#     '05': 'in progress',
#     '04': 'completed'
# }

# Extract a list of unique values (sorted alphabetically) from the project_ids dictionary and print it to the console.

# Expected result:
# ['completed', 'in progress', 'open']
# ---------------------------------------------------------

project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

# extract values and convert them in set
a = set(project_ids.values())

# set will take only unique values and create a list
b = list(a.difference())

#Sort the list by asc
b.sort()
print(b)
