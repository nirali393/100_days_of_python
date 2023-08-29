# -------------------Exercise 3-------------------
# The geometric sequence is given with the following formula: an = 8.2^(n-1)

# Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.

# Expected result: The sum of the first 6 elements of the sequence is: 504.0
# --------------------------------------------------

a1 = 8
a2 = 8 * 2
n = 6
 
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
 
print(f'The sum of the first 6 elements of the sequence is: {s6}')
