# -------------------Exercise 3-------------------
# The following text is given:
# text = '      100 Days of Code   '

# Using the appropriate method remove whitespace characters around the text. Print the result to the console.
# Expected result: 100 Days of Code
# --------------------------------------------------

text = '      100 Days of Code   '

#strip will remove left and right white space.
print(text.strip())

# We can also make sure by counting the length of the string
print(len(text.strip()))
