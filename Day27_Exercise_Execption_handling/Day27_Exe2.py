# -------------------Exercise 2----------------------------
# Sometimes we need to open a file without knowing if such a file exists. When file doesn't exist the FileNotFoundError is raised.
# Using the try... except... clause, handle with this problem.
# Use this code snippet to read the content of the file:

# with open('file.txt', 'r') as file:
#     content = file.read()

# Try to open file.txt using the above code. If the file.txt does not exist, print to the console following message:
# 'File not found.'
# ---------------------------------------------------------

try:
    with open('file.txt', 'r') as file:
        content = file.read()
        print(content)

except file.txt:
    print("File not found")

