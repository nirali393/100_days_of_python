# -------------------Exercise 1----------------------------
# Implement a function called maximum() that returns the maximum of two numbers. 
# Use conditional statement.
# ---------------------------------------------------------
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
print(maximum(a, b))
