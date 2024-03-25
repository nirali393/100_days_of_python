# -------------------Exercise 2---------------------------- 
# Using the math built-in module, implement the function called sigmoid() expressed by the formula:
# f(x) = 1/[1+(e)^-x)
# Note: All you have to do is implement the function.
# ---------------------------------------------------------
import math
 
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
sim = sigmoid(3)
print(sim)