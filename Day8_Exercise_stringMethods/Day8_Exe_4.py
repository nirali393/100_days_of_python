# -------------------Exercise 4-------------------
# From the given url:
# url = (
#     'https://e-smartdata.teachable.com/'
#     'p/sciezka-data-scientist-machine-learning-engineer'
# )
# extract the slug after the last character '/'. Then replace all dashes with spaces and print the result to the console as shown below.

# Expected result: sciezka data scientist machine learning engineer
# --------------------------------------------------

url = (
    'https://e-smartdata.teachable.com/'
    'p/sciezka-data-scientist-machine-learning-engineer'
)

# a will search from the end for "/" and will store the value.
a = url.split("/")[-1]

# this will replace - to " " and print the string
print(a.replace("-", " "))
