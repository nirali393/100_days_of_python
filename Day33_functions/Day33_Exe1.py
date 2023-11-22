# -------------------Exercise 1----------------------------
# Implement a function called maximum() that returns the maximum of two numbers. 
# Use conditional statement.
# ---------------------------------------------------------

def maximum():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    if num1 > num2:
        print(num1)
    else: 
        print(num2)

maximum()
