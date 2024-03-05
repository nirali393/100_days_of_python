# -------------------Exercise 2---------------------------- 
# The contents of the file plw.txt were loaded as follows:
# with open('plw.txt', 'r') as file:
#     lines = file.read().splitlines()

# Tasks to perform:
# 1. Get rid of blank lines.
# 2. Split each line into tokens/words as shown below and print result to the console.
# ---------------------------------------------------------

with open('plw.txt', 'r') as file:
    lines = file.read().splitlines()
lines = [line for line in lines if len(line) > 0]
lines = [line.split() for line in lines]
print(lines)