# -------------------Exercise 3---------------------------- 
# Using the previous exercise, implement a function called detect_class(), which in the place of the highest probability value in the row puts 1 and beyond 0 (see below).

# We assume that the user passes the matrix as a nested list with non-negative elements and sum in each row equal to 1.
# Argument:
# array - nested list (two-dimensional matrix, row adds up to one)

# Example:
# [IN]: detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]]) 
# [OUT]: [[0, 1, 0, 0], [0, 0, 1, 0]]

# [IN]: detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.3, 0.3, 0.4]]) 
# [OUT]: [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# Note: You only need to implement this function.
# ---------------------------------------------------------

def detect_class(array):
    result = []
    for item in array:
        max_val = max(item)
        empty = [0] * len(item)
        for idx, val in enumerate(item):
            if val == max_val:
                empty[idx] = 1
                result.append(empty)
    return result

array_list = ([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]]) 
print(detect_class(array_list))