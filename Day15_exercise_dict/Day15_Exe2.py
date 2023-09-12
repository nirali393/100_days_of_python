# -------------------Exercise 2--------------------
# The following dictionary is given:

# stocks = {
#     'MSFT.US': {'Microsoft Corp': 184},
#     'AAPL.US': {'Apple Inc': 310},
#     'MMM.US': {'3M Co': 148}
# }

# Extract the value for the key 'AAPL.US' and print it to the console.

# Expected result:
# {'Apple Inc': 310}
# --------------------------------------------------

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}

print(stocks.get('AAPL.US'))
