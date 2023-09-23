# -------------------Exercise 3----------------------------
# Write a program that compares two lists and returns True if the lists contain at least one of the same element. Otherwise, it will return False.

# Use break statement in the solution and print result to the console.

# Lists:

# list1 = [1, 2, 0]
# list2 = [4, 5, 6, 1]

# Expected result:True
# -----------------------------------------------------------

list1 = [7, 2, 0]
list2 = [4, 5, 6, 1]

for no1 in list1:
    for no2 in list2:
        if no1 == no2:
            print('True')
        else:
            print('False')
            