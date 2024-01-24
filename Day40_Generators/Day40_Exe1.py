# -------------------Exercise 1----------------------------
# Implement a generator named file_gen(), which selects only those names of files with the '.txt' extension from the list.

# Example:

# [IN]: fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
# [IN]: list(file_gen(fnames))
# [OUT]: ['data1.txt', 'data2.txt', 'data3.txt']

# Note! All you have to do is define a generator. 
# ---------------------------------------------------------

def file_gen(filenames):
    for fname in filenames:
        if fname.endswith('.txt'):
            yield fname

fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
result = list(file_gen(fnames))
print(result)
