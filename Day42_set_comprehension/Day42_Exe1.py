# -------------------Exercise 1---------------------------- 
# Consider a three-roll of the dice. 
# Create the probability space (omega) and 
# calculate the probability of obtaining three values which the sum is divisible by 7.
# Use set comprehension. 
# Round the result to two decimal places and 
# print the result to the console as shown below.
# Probability: 0.14
# ---------------------------------------------------------

omega = {(i,j,k): i+j+k for i in range(1,7) for j in range(1,7) for k in range(1,7)}
no_of_comination = len([(k, v) for k,v in omega.items() if v%7 == 0])
print(f"Probability: {round(no_of_comination/len(omega),2)}")