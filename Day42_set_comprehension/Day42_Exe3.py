# -------------------Exercise 3---------------------------- 
# We roll the symmetrical dice three times. 
# Calculate the probability of the following:
#  - odd number of points in each roll
# Use set comprehension. 
# Round the result to three decimal places and 
# print to the console as shown below.
# Probability: 0.125
# ---------------------------------------------------------

omega = {(i,j,k): i+j+k for i in range(1,7) for j in range(1,7) for k in range(1,7)}
no_of_f_outcome = sum(1 for i,j,k in omega if i % 2 != 0 and j % 2 != 0 and k % 2 != 0)
print(f" Probability: {round(no_of_f_outcome/len(omega),3)}")
