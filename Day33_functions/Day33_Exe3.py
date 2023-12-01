# -------------------Exercise 3----------------------------
# Implement a function called multi(), which accepts an iterable object (list, tuple) as an argument and returns the product of all elements of this iterable object.

# [IN]: multi((-4, 6, 2))
# [OUT]: -48


# [IN]: multi([4, 2, -5])
# [OUT]: -40
# ---------------------------------------------------------

def multi(iterable):
    result = 1
    for element in iterable:
        result *= element
    return result

result1 = multi((-4, 6, 2))
result2 = multi([4, 2, -5])

print(result1)  
print(result2) 
