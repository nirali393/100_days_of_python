# -------------------Exercise 2---------------------------- 
# Calculate the probability that in three throws of symmetrical cubic dice, 
# the sum of the squares of points will be divisible by 3. 
# Use set comprehension. 
# Round the result to the fourth decimal place and 
# print the result to the console as shown below.
# Probability: x.xxxx
# ---------------------------------------------------------
omega = {(i,j,k): pow(i,2)+pow(j,2)+pow(k,2) for i in range(1,7) for j in range(1,7) for k in range(1,7) }
no_of_f_outcome = sum(1 for v in omega.values() if v%3 ==0)
print(f"Probability: {round(no_of_f_outcome/len(omega),4)}")
