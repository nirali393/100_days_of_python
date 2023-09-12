# -------------------Exercise 3-------------------
# The following tuple is given (name, age):
# info = (('Monica', 19), ('Tom', 21), ('John', 18))

# Sort this tuple:
# ascending by age descending by age And print the result to the console as shown below.

# Expected result:
# Ascending: (('John', 18), ('Monica', 19), ('Tom', 21))
# Descending: (('Tom', 21), ('Monica', 19), ('John', 18))
# --------------------------------------------------

info = (('Monica', 19), ('Tom', 21), ('John', 18))
i = 0

asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))

print(f'Ascending: {asc}')
print(f'Descending: {desc}')
