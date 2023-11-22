# -------------------Exercise 2----------------------------
# Implement a function called maximum() that returns the maximum of three numbers. 
# Use conditional statement.
# ---------------------------------------------------------

def maximum(a,b,c):
    if a>b & a>c:
        print(a)
    elif b>a & b>c:
        print(b)
    else:
        print(c)
