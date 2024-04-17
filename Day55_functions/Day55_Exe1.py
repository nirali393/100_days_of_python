# -------------------Exercise 1---------------------------- 
# Implement a function called identity(), which takes a natural number as an argument and return an identity matrix (nested list).
# Example:
# [IN]: identity(2)
# [OUT]: [[1, 0], [0, 1]]
# [IN]: identity(3)
# [OUT]: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# [IN]: identity(4)
# [OUT]: [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
# Note: You only need to implement this function.
# ---------------------------------------------------------


def identity(n):
    array = [[0] * n for i in range(n)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array

n_input = int(input("Enter a number: "))
result = identity(n_input)
print(result)