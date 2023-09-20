# -------------------Exercise 1----------------------------
# Write a program that finds all two-digit numbers divisible by 11 and indivisible by 3 (use a for loop). Print the result to the console as comma-separated values as shown below.

# Expected result:
# 11,22,44,55,77,88
# ---------------------------------------------------------

num = []
for i in range(1,100):
    if i % 11 == 0 and not i % 3 ==0:
        num.append(i)
print(num)
