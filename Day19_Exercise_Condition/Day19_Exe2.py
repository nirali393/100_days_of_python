# -------------------Exercise 2----------------------------
# The following password is given:

# password = 'cskdnjcasa#!'

# Check if the password has at least 11 characters and contains the special character '!'.

# If so, print 'Password correct', otherwise 'Password incorrect'.

# Expected result: Password correct
# ------------------------------------------------------------

password = 'cskdnjcasa#!'

if len(password) >=11 and password.count('!') != 0:
    print('Password correct')
else:
    print('Password incorrect')
