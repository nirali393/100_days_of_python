# -------------------Exercise 1----------------------------
# Implement a function count_str(), which returns the number of str objects in an iterable object (list, tuple, set).
# Example:

# [IN]: count_str(['p', 2, 4.3, None])
# [OUT]: 1

# [IN]: count_str({'p', 2, 4.3, True, 'True', None})
# [OUT]: 2
# ---------------------------------------------------------

mixed_list = [1, 'apple', 3.14, 'banana', True, 'orange', 42]

def count_str(inpup_list):
    try:
        strings_only = []
        for item in inpup_list:
            if isinstance(item, str):
                strings_only.append(item)

        return strings_only
    except ValueError:
        pass

filtered_list = count_str(mixed_list)
print(filtered_list)
