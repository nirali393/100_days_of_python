# -------------------Exercise 1----------------------------
# The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:

# with open('playway.csv', 'r') as file:
#     content = file.read().splitlines()

# Find the highest volume for a given month and print the result to the console as shown below.
# # ----------------------------------------------------------

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
    # print(content)
    temp_var = 0

    for i in content[1:]:
        sep_str = int(i.split(',')[5])
        # print(sep_str)

        if sep_str> temp_var:
            
            temp_var = sep_str
            
        else:
            continue
print(temp_var)

        