# -------------------Exercise 2-------------------------
# From the following text: string = 'PKV-89415-PLN'
# extract the code containing the first three and last three characters. Print the result to the console.

# Expected result: PKVPLN
# ------------------------------------------------------

string = 'PKV-89415-PLN'

list1 = string[:3]
list2 = string[-3:]

print(list1+list2)
