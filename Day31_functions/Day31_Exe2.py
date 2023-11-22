# -------------------Exercise 2----------------------------
# The following variables are given:
# var1 = 'Python'
# var2 = ('Python')
# var3 = ('Python',)
# var4 = ['Python']
# var5 = {'Python'}
# Using the appropriate function, check if the variables are instances of tuple class. Print the result to the console as shown below.

# Tip: Use the isinstance() built-in function.
# ---------------------------------------------------------

var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

var = [var1, var2, var3, var4, var5]

for i in var:
    if isinstance(i, tuple):
        print(True)
        
    else:
        print(False)