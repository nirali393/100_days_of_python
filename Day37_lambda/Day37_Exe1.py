# -------------------Exercise 1----------------------------
# Implement the function is_palindrome(), which takes as an argument str object and checks if this object is a palindrome (expression that sounds the same from left to right and from right to left).
# If so, the function should return True, on the contrary False.

# Example:

# [IN]: is_palindrome('level')
# [OUT]: True

# [IN]: is_palindrome('python')
# [OUT]: False
# ---------------------------------------------------------

# in_list = 'level'
# center_point = len(in_list) // 2
# temp_list = []

# def is_palindrome(in_list):
#     for f in range(center_point):
#         if f >= center_point:
#             break
#         else:
#             first = in_list[f]
#             last = in_list[-(f+1)]
#             if first == last:
#                 temp_list.append(True)
#             else:
#                 temp_list.append(False)
#     if all(temp_list):
#         print(True)
#     else:
#         print(False)

# is_palindrome(in_list)

def is_palindrome(in_list):
    rev_str = in_list[::-1]
    if rev_str == in_list:
        return True
    else:
        return False


in_list = 'level'
result = is_palindrome(in_list)
print(result)