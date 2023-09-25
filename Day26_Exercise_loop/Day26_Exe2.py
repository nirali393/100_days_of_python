# -------------------Exercise 2-----------------------------
# Write a program that prints to the console the first ten prime numbers separated by a comma.

# Tip: Use a while loop with break statement.
# Expected result:
# 2,3,5,7,11,13,17,19,23,29
# ----------------------------------------------------------

counter = 0
number = 2
prime = []
 
while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1
 
 
print(','.join(prime))

