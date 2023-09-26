# -------------------Exercise 2----------------------------
# The following dictionary is given:

# users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}

# Try printing the value for the key:
# user_id = '004'

# In case of a KeyError, print to the console the following message:
# 'The 004 key is not in the dictionary. Adding key ...'
# Then add this key to the dictionary with the value None and print the users dictionary to the console.

# Expected result:
# The 004 key is not in the dictionary. Adding key ...
# {'001': 'Mark', '002': 'Monica', '003': 'Jacob', '004': None}
# ---------------------------------------------------------

users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'

try:
    print(users['004'])
except KeyError:
    print('The 004 key is not in the dictionary. Adding key ...')
    users['004'] = None
    print(users)