# -------------------Exercise 1---------------------------- 
# The following dictionary is given:
# stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
# Use dict comprehension to replace values with keys and print the result to the console.
# Expected result:
# {'001': 'Boombit', '002': 'CD Projekt', '003': 'Playway'}
# ---------------------------------------------------------

stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
new_stock = {v:k for k,v in stocks.items()}
print(new_stock)
