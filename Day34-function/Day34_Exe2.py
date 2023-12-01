# -------------------Exercise 2----------------------------
# Implement a function called filter_ge_6() that takes a list of words and returns list of words with the length greater than or equal to 6 characters.
# Example:

# [IN]: filter_ge_6(['programming', 'python', 'java', 'sql'])
# [OUT]: ['programming', 'python']

# [IN]: filter_ge_6(['java', 'sql'])
# [OUT]: []
# ---------------------------------------------------------


# user input in list (l)
arr = input("Enter Words: ")
l = list(map(str, arr.split(' ')))

# function
def filter_ge_6():

    #list to store 6 letter word or more
    new_list = []

    # for loop to itrate over each element in list l
    for a in l:

        # if condition for more then 6 letter word
        if len(a) >=6:

            # appen the list
            new_list.append(a)
    print(new_list)

# cfunction call
filter_ge_6()
