# -------------------Exercise 3---------------------------- 
# Create a list consisting of dictionaries mapping consecutive digits from 1 to 9 inclusive to their respective k-th powers, for k = 1, 2, 3.

# Print the result to the console as shown below.
# Formatted result:
# [{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9},
#  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81},
#  {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}]

# Expected result:
# [{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}, {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}]
# ---------------------------------------------------------
one_dict = {i : pow(i,1) for i in range(1,10)}
two_dict = {j : pow(j,1) for j in range(1,10)}
three_dict = {k : pow(k,1) for k in range(1,10)}

one_list = [one_dict, two_dict, three_dict]
print(one_list)