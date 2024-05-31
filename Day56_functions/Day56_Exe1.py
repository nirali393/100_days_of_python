# -------------------Exercise 1---------------------------- 
# Implement a function called transpose() that transposes the two-dimensional matrix (nested list).
# Argument:
# array - nested list (two-dimensional matrix)

# Example:
# [IN]: transpose([[1, 2, 3], [4, 5, 6]])
# [OUT]: [[1, 4], [2, 5], [3, 6]]

# [IN]: transpose([[1, 2], [3, 4], [5, 6]])
# [OUT]: [[1, 3, 5], [2, 4, 6]]

# [IN]: transpose([[1, 2, 3, 4], [5, 6, 7, 8]])
# [OUT]: [[1, 5], [2, 6], [3, 7], [4, 8]]
# Note: You only need to implement this function.
# ---------------------------------------------------------

def transpose(array):
    width = len(array[0])
    result = []
    for i in range(width):
        pair = []
        for item in array:
            pair.append(item[i])
        result.append(pair)
    return result

array = [[1, 2], [3, 4], [5, 6]]
print(transpose(array))
