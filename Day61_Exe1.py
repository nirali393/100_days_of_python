# -------------------Exercise 1---------------------------- 
# Using the built-in os module in your working directory create a directory called documents. Then, in the documents directory, create 12 directories for each month with the names 01_sales, ..., 12_sales, respectively.
# In response, print directory names sorted alphabetically in the documents directory to the console.

# Tip:
# >>> help(os.mkdir)
# Help on built-in function mkdir in module nt:
 
# mkdir(path, mode=511, *, dir_fd=None)
#     Create a directory.
    
#     If dir_fd is not None, it should be a file descriptor open to a directory,
#       and path should be relative; path will then be relative to that directory.
#     dir_fd may not be implemented on your platform.
#       If it is unavailable, using it will raise a NotImplementedError.
    
#     The mode argument is ignored on Windows.
    
# >>> help(os.listdir)
# Help on built-in function listdir in module nt:
 
# listdir(path=None)
#     Return a list containing the names of the files in the directory.
    
#     path can be specified as either str, bytes, or a path-like object.  If path is bytes,
#       the filenames returned will also be bytes; in all other circumstances
#       the filenames returned will be str.
#     If path is None, uses the path='.'.
#     On some platforms, path may also be specified as an open file descriptor;\
#       the file descriptor must refer to a directory.
#       If this functionality is unavailable, using it raises NotImplementedError.
    
#     The list is in arbitrary order.  It does not include the special
#     entries '.' and '..' even if they are present in the directory.

# Expected result:
# ['01_sales', '02_sales', '03_sales', '04_sales', '05_sales', '06_sales', '07_sales', '08_sales', '09_sales', '10_sales', '11_sales', '12_sales']
# ---------------------------------------------------------

import os
 
 
os.mkdir('documents')
dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
 
for dirname in dirnames:
    path = os.path.join('documents', dirname)
    os.mkdir(path)
 
 
print(sorted(os.listdir('documents')))