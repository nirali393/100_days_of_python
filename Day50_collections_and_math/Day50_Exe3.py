# -------------------Exercise 3---------------------------- 
# Using the random built-in module set the random seed as follows:
# random.seed(12)
# And select randomly (pseudo-randomly) an item from the list below:
# items = ['python', 'java', 'sql', 'c++', 'c']

# Print the result to the console.
# Expected result:
# c++
# ---------------------------------------------------------

import random


random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
# enter your solution here
result = random.choice(items)
print(result)