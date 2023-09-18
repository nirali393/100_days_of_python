# -------------------Exercise 4-------------------
# The following paths are given:
# path1 = (
#     'https://e-smartdata.teachable.com/p/'
#     'sciezka-data-scientist-machine-learning-engineer'
# )
# path2 = (
#     'https://e-smartdata.teachable.com/p/'
#     'sciezka-data-scientist-deep-learning-engineer'
# )
# path3 = (
#     'https://e-smartdata.teachable.com/p/'
#     'sciezka-bi-analyst-data-analyst'
# )

# Using the appropriate method, find the word 'scientist' in the given paths, returning the index for the first letter of the found word. If the word is not in the path, the method should return -1. Print the result to the console as shown below.
# Expected result:
# path1: 49
# path2: 49
# path3: -1
# --------------------------------------------------

path1 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-data-scientist-machine-learning-engineer'
)
path2 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-data-scientist-deep-learning-engineer'
)
path3 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-bi-analyst-data-analyst'
)

print(path1.find("scientist"))
print(path2.find("scientist"))
print(path3.find("scientist"))
