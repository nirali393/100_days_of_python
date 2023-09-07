# -------------------Exercise 1-------------------
# The following codes are given:
# code1 = 'FVNISJND-20'
# code2 = 'FVNISJND20'

# Using the appropriate method, check whether the codes consist only of alphanumeric characters (numbers + letters). Print the result to the console as shown below.
# Expected result:
# code1: False
# code2: True
# --------------------------------------------------

code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'


#isalnum() will check if the string is alphanumeric
print(code1.isalnum())
print(code2.isalnum())
