# -------------------Exercise 1---------------------------- 
# Consider the two-roll of the dice. 
# Create the probability space (omega) and 
# count the probability of getting a sum of points higher than 10. 
# Use set comprehension.
# ---------------------------------------------------------
set_range = range(1,7)
t = 0

omega = {(i,j): i+j for i in set_range for j in set_range}
count_of_occurance = len(set(val for val in omega.values() if val>10))
result = (count_of_occurance+1)/len(omega)

print(f" Probability: {round(result,4)}")