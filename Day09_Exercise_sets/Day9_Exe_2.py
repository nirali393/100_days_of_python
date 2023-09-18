# -------------------Exercise 2-------------------
# The following text is given:
# text = 'Programming in python.'

# Follow the next steps:
# Change all letters to lowercase.
# Delete spaces and period.
# Create a set consisting of all letters in the text and assign to letters variable
# Using the appropriate method for sets, remove all vowels from letters set:

# vowels = {'a', 'e', 'i', 'o', 'u'}
#  5. Print the number of items in the letters set as shown below.
# Expected result: Number of items: 8
# --------------------------------------------------

text = 'Programming in python.'     #str data type
vowels = {'a', 'e', 'i', 'o', 'u'}  #set data type

a = text.lower()                    #lower the test(str) 
b = a.replace(" ", "")              #replace space with no space
c = b.replace(".", "")              #replace . with no .
c_string = set(c)                     # c_string will store the converted string 

c_string.difference_update(vowels)    # difference_update() will delete dublicate from the c_string
print(f'Number of items:{len(c_string)}')  #print the length of the c_string
