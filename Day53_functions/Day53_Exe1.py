# -------------------Exercise 3---------------------------- 
# Implement a function called relu() (ReLU - Rectified Linear Unit). This function is used in neural networks and is given by the following formula:

# Note: You only need to implement this function.
# ---------------------------------------------------------

def relu(x):
    return max(0, x)

in_num = int(input("Enter a number: "))
result = relu(in_num)
print(result)