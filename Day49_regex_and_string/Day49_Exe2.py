# -------------------Exercise 2---------------------------- 
# Using the built-in module for regular expressions, split the following text by whitespace (spaces):
# text = 'Programming in Python - from A to Z'

# Print the result to the console.

# Tip: Use the re.split() function and the regular expression '\s+'.
# Expected result:
# ['Programming', 'in', 'Python', '-', 'from', 'A', 'to', 'Z']
# ---------------------------------------------------------

import re
 
text = 'Programming in Python - from A to Z'
result = re.split(pattern=r"\s+", string=text)

print(result)