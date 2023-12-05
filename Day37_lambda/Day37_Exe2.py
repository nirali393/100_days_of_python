# -------------------Exercise 2----------------------------
# The following list of words is given:
# stocks = ['playway', 'boombit', 'cd projekt']

# Using the map() function and the lambda expression, transform the given list into a list containing the lengths of each word and print it to the console.

# Expected result:
# [7, 7, 10]
# ---------------------------------------------------------

stocks = ['playway', 'boombit', 'cd projekt']

def map_length(stocks):
    return list(map(lambda element: len(element), stocks))
result = map_length(stocks)
print(result)
