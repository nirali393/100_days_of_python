# -------------------Exercise 1----------------------------
# Sort the given list of dictionaries by price key:

# stocks = [
#     {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
#     {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
#     {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
# ]

# Print sorted list to the console.

# Formatted result:
# [{'index': 'sWIG80', 'name': 'BBT', 'price': 22},
#  {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
#  {'index': 'mWIG40', 'name': 'PLW', 'price': 309}]

# Expected result:
# [{'index': 'sWIG80', 'name': 'BBT', 'price': 22}, {'index': 'mWIG40', 'name': 'TEN', 'price': 304}, {'index': 'mWIG40', 'name': 'PLW', 'price': 309}]
# ---------------------------------------------------------

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

stocks.sort(key = lambda stock: stock['price'])
print(stocks)
