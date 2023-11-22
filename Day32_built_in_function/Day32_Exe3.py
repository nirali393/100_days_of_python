# -------------------Exercise 3----------------------------
# Count the number of ones in the binary representation of number:
# number = 234
# Print the result to the console.
# Tip: Use the bin() built-in function.
# ---------------------------------------------------------

number = 234
string_bin = str(bin(number))

print(string_bin.count('1'))
