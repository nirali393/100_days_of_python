# -------------------Exercise 1----------------------------
# The list of names is given (one is missing):
# names = ['Jack', 'Leon', 'Alice', None, 'Bob']

# Using the continue statement, print only the correct names to the console as shown below.

# Expected result:
# Jack
# Leon
# Alice
# Bob
# --------------------------------------------------------

names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for i in names:
    if i is None:
        continue
    else:
        print(i)
         