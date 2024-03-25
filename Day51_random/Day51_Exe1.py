# -------------------Exercise 1---------------------------- 
# random.seed(15)
# And shuffle (pseudo-randomly) items in the following list:

# items = ['python', 'java', 'sql', 'c++', 'c']
# In response, print the list to the console.

# Expected result:
# ['c', 'c++', 'sql', 'python', 'java']
# ---------------------------------------------------------
import random

random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']
# enter your solution here

random.shuffle(items)

print(items)