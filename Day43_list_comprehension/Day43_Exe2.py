# -------------------Exercise 2---------------------------- 
# The list of product prices is given:
# net_price = [5.5 4.0, 9.0, 10.0]
# The VAT for these products is equal to 23%:
#     tax = 0.23
# Using the list comprehension, calculate the gross price for each product.Round the price to two decimal places and print result to the console.
#     Expected result:
# {6.76, 4.92, 11.07, 12.3}
# ---------------------------------------------------------

tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross_price = [round(price*(1+tax),2) for price in net_price]
print(gross_price)
