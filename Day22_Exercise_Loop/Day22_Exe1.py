# -------------------Exercise 1----------------------------
# The following text is given:
# text = 'Python is a very popular programming language'

# Write a program which extracts exactly the first four words as a list. Standardize each word, i.e. replace uppercase letters with lowercase. Present the result in a list and print to the console as shown below.

# Expected result:
# ['python', 'is', 'a', 'very']
# ----------------------------------------------------------

text = 'Python is a very popular programming language'
new_list = []

words = text.split(" ")
four_word = words[0:4]

for word in four_word:
    a = str(word.lower())
    new_list.append(a)

print(new_list)
