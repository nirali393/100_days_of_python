# -------------------Exercise 2---------------------------- 
# Using the built-in module for regular expressions, find all digits in the following text:
# string = 'Python 3.8'

# Print the result to the console.

# Tip: Use the findall() function and the regular expression '\d'
# Expected result:
# ['3', '8']
# ---------------------------------------------------------

string = 'Python 3.8'
no_list = [char for char in string if char.isdigit()]
print(no_list)