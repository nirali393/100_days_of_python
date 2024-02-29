# -------------------Exercise 3---------------------------- 
# Consider the two-roll of the dice. 
# Create the probability space (omega) and 
# calculate the probability of getting a sum of squares higher or equal to 45. 
# Use set comprehension. 
# Round the result to two decimal places and 
# print the result to the console as shown below.
# Probability: 0.22
# ---------------------------------------------------------


omega = {(i,j): pow(i,2)+pow(j,2) for i in range(1,7) for j in range(1,7)}
occurance_of_event = len([value for value in omega.values() if value >=45])
prob = 0
print(f"Probability: {round(occurance_of_event/len(omega),2)}")

