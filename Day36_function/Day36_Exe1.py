# -------------------Exercise 1----------------------------
# Implement a function is_distinct() to check if the list contains unique values.

# Example:

# [IN]: is_distinct([1, 2, 3])
# [OUT]: True

# [IN]: is_distinct([1, 2, 3, 3])
# [OUT]: False
# ---------------------------------------------------------

def is_distinct(in_list):
    try:
        x = list(set(in_list))
        temp_list = []

        for v in x:
            if in_line.count(v) > 1:
                temp_list.append(v)

        if len(temp_list) >=1:
            return False
        else:
            return True
    except:
        pass


# def is_distinct(items):
#     return len(items) == len(set(items))

in_line = [1, 2, 3]
result = is_distinct(in_line)
print(result)


