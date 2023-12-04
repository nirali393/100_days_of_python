# -------------------Exercise 2----------------------------
# Implement a function count_str(), which returns the number of str objects with a length more than 2 characters from an iterable object (list, tuple, set).

# Example:

# [IN]: count_str([1, '#hello', '', 'python', 'go'])
# [OUT]: 2

# [IN]: count_str([1, 2, 3, 'python'])
# [OUT]: 1
# ---------------------------------------------------------


# Function 
def count_str(val_str):

    # list to store str value and 2 >
    count_str = []
    try:
        for v in val_str:
            if isinstance(v,str) and len(v) > 2:
                count_str.append(v)
    except ValueError:
        print("ERROR")
    return len(count_str)


val_str = [1, '#hello', '', 'python', 'go']
result = count_str(val_str)

print(result)