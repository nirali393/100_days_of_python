# -------------------Exercise 1---------------------------- 
# The gaming.txt file is attached to this exercise. 
# This file has been loaded into the text variable. 
# From the text list delete all newline characters. Then delete empty lines and print the text to the console.
# ---------------------------------------------------------
with open('gaming.txt','r') as file:
    text = file.readlines()

text = [line.replace('\n', '') for line in text]
text = [line for line in text if len(line) > 0]
print(text)
