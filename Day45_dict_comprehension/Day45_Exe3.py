# -------------------Exercise 3---------------------------- 
# The following list is given:
# stocks = ['Playway', 'CD Projekt', 'Boombit']
# Use dict comprehension to build a dictionary that maps company names to the number of characters of its name and print the result to the console.

# Expected result:
# {'Playway': 7, 'CD Projekt': 10, 'Boombit': 7}
# ---------------------------------------------------------

stocks = ['Playway', 'CD Projekt', 'Boombit']
char_dict = {stock : len(stock) for stock in stocks}
print(char_dict)