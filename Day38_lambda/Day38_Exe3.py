# -------------------Exercise 3----------------------------
# The following list is given:

# stocks = [
#     {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
#     {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
#     {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
# ]
# Extract companies from the 'mWIG40' index and print the result to the console.
# ---------------------------------------------------------

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

def company():
    print(list(filter(lambda item: item['index'] == 'mWIG40', stocks)))

company()