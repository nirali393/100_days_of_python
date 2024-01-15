# -------------------Exercise 1----------------------------
# The following list is given:

# stocks = [
#     {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
#     {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
#     {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
# ]

# Convert the list to a list of boolean values (True, False). True if the company belongs to the 'mWIG40' index, False on the contrary and print the result to the console.
# ---------------------------------------------------------

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(list(map(lambda x: x['index'] == 'mWIG40', stocks)))
