# -------------------Exercise 3---------------------------- 
# Implement a function called trace() that returns the trace of the matrix. The matrix must be a square matrix.

# Argument:
# array - nested list (two-dimensional matrix)
# Example:
# [IN]: trace([[1]])
# [OUT]: 1
# [IN]: trace([[1, 2], [4, 2]])
# [OUT]: 3
# [IN]: trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]])
# [OUT]: 7
# Note: You only need to implement this function.
# ---------------------------------------------------------

def trace(array):
    total = 0
    for idx, item in enumerate(array):
        total += item[idx]
    return total

result = trace([[1]])
print(result)