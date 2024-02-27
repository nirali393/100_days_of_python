# -------------------Exercise 1---------------------------- 
# Consider the two-roll of the dice. 
# Create the probability space (omega) and 
# count the probability of getting a sum of points higher than 10. 
# Use set comprehension.
# ---------------------------------------------------------

dice_outcomes = range(1, 7)  # Possible outcomes of a single die

omega = {}
temp = 0
for i in dice_outcomes:
    for j in dice_outcomes:
        omega[(i, j)] = i + j
        if i + j > 10:
            temp +=1

result = temp/len(omega)
print(f"Probability {result}" )