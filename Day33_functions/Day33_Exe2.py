# -------------------Exercise 2----------------------------
# Implement a function called maximum() that returns the maximum of three numbers. 
# Use conditional statement.
# ---------------------------------------------------------

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

print(maximum(a, b, c))
