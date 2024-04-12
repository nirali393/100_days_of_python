# -------------------Exercise 2---------------------------- 
# Implement a function called arange() that takes three parameters: start, stop, step and generates a list consisting of integers greater than or equal to start and less than stop. The step parameter defaults to 1 indicates the size of the step.

# Example:
# [IN]: arange(0, 10)
# [OUT]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [IN]: arange(0, 10, 2)
# [OUT]: [0, 2, 4, 6, 8]

# Note: You only need to implement this function.
# ---------------------------------------------------------

def arange(start, stop, step=1):
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result

result = arange(0,10)
print(result)