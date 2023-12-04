# -------------------Exercise 3----------------------------
# Implement a function remove_duplicates() that removes duplicates from the list (the order of the items in the list does not have to be kept).

# Example:

# [IN]: remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4])
# [OUT]: [1, 2, 3, 4, 5]

# [IN]: remove_duplicates([1, 1, 1, 1])
# [OUT]: [1]
# ---------------------------------------------------------

# Function

def remove_duplicates(in_list):
    try:
        in_list = list(dict.fromkeys(in_list))   
        in_list.sort()            
    except ValueError:
        print("!!! ERROR !!!")
    return in_list

in_list = [1, 5, 3, 2, 2, 4, 2, 4]
result = remove_duplicates(in_list)

print(result)
