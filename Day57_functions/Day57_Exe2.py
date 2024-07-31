# -------------------Exercise 2---------------------------- 
# Implement a function called count_none() that counts all missing values in the list.
# Example:
# [IN]: count_none([1, None, None, 5, None, 2])
# [OUT]: 3
# Note: You only need to implement this function.
# ---------------------------------------------------------

def count_none(items):
    counter = 0
    for item in items:
        if not item:
            counter += 1
    return counter

count_list = [1, None, None, 5, None, 2]
print(count_none(count_list))