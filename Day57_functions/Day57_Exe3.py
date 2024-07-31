# -------------------Exercise 3---------------------------- 
# Implement a function top_n() which extracts top n largest values from the given list.
# Arguments:
# items - list of values
# n - top n elements to extract
# Example:
# [IN]: top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3)
# [OUT]: [10, 9, 8]
# Note: You only need to implement this function.
# ---------------------------------------------------------

def top_n(items, n):
    items.sort(reverse=True)
    return items[:n]

top_list =[4, 5, 2, 9, 5, 2, 8, 2, 8, 10]
n = 3
print(top_n(top_list, n))