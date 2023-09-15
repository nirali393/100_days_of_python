# -------------------Exercise 3----------------------------
# The following dictionary is given:
# users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}

# Try to print value for key '004'.
# In this exercise use the dict.get() method. When the key is not in the dictionary set default value to the string 'indefinite'.
# Expected result: 'indefinite'
# ---------------------------------------------------------

users = {'001': 'Mark',
        '002': 'Monica',
        '003': 'Jacob'}

users.setdefault('004', 'indefinite')
print(users.get('004'))
