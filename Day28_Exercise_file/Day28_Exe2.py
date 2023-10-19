# -------------------Exercise 2----------------------------
# Read the currencies.txt file. 
# Each line has a different currency pair. 
# Create a list with the names of currency pairs containing the 'USD' symbol.

# Expected result:
# ['ARSUSD', 'AUDUSD']
# ---------------------------------------------------------

temp_list = []

f = open("currencies.txt", "r")
lines = f.read().split('\n')
for currency in lines:
    if 'USD' in currency:
        temp_list.append(currency)
print(temp_list)
         
