# -------------------Exercise 1----------------------------
# Implement a function map_longest() that accepts the list of words and return the length of the longest word in this list.
# [IN]: map_longest(['python', 'sql'])
# [OUT]: 6


# [IN]: map_longest(['java', 'sql', 'r'])
# [OUT]: 4
# ---------------------------------------------------------

# taking array from user and stored in l
arr = input("Enter Words in list seperated by a comma: ")
l = list(map(str,arr.split(' ')))     # map function will itrate on list and seperate by ,
print(l)
# functio
def map_longest():

    # len will count the length of each elemnt in alist and stored in length_l
    length_l=list(map(len, l))

    # max function to get the maximum no. from the list length_l
    result = max(length_l)
    print(result)

# calling the function
map_longest()
