# -------------------Exercise 3-------------------
# The following text is given:
# text = 'Python programming'

# Standardize the text (replace uppercase letters with lowercase). Then create a list of unique characters in the text. Remove the space from this list and sort from a to z. After all print the list to the console.

# Tip: You can use a set to generate unique characters.
# Expected result:
# ['a', 'g', 'h', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'y']
#-------------------------------------------------

# text data type is str
text = 'Python programming'

# replace space with no space
s = text.replace(" ", "")

# convert to set and lower the upper case
a = set(s.lower())

# convert to list and only take unique
list_text = list(a.difference())

# sort the list by asc
list_text.sort()

print(list_text)
