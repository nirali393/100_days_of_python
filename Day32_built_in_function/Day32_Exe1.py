# -------------------Exercise 1----------------------------
# Two tuples are given:
# ticker = ('TEN', 'PLW', 'CDR')
# full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

# Using the appropriate built-in function, create a list consisting of tuples (ticker, full_name) and print the result to the console as shown below.
# Tip: Use the zip() function.
# --------------------------------------------------------

ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

new_list = zip(ticker, full_name)
print(list(new_list))
