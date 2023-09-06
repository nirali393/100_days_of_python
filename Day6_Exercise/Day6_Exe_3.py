# -------------------Exercise 3-------------------
# The following paths are given:
# path1 = 'youtube.com/watch?v=5EhRztVxums'
# path2 = 'google.com/search?q=car'

# Using the appropriate method check if the paths refer to YouTube (e.g. start with 'youtube'). Print the result to the console as shown below.
# Expected result:
# path1: True
# path2: False
# --------------------------------------------------

path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

print(f"path1: {path1.find('youtube')}")
print(f"path2: {path2.find('youtube')}")
