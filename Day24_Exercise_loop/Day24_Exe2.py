# -------------------Exercise 2----------------------------
# A list of names entered by users into the system is given below (without validation process):

# names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

# Iterate through the names list and check if each name is correct (contains only letters). If so, print to the console following message: f'Hello {name}!' otherwise do nothing.
# Tip: Use the str.isalpha() method.

# Expected result:
# Hello Jack!
# Hello Leon!
# Hello Alice!
# Hello Bob!
# ----------------------------------------------------------
import re
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for i in names:
    if re.match("^[a-zA-Z]+$", i):
        print(f'Hello {i}!')