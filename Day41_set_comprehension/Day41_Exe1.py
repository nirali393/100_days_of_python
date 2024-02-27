# -------------------Exercise 1---------------------------- 
# Consider the two-roll of the dice. 
# Create the probability space (omega) and 
# count the probability of getting a sum of points higher than 10. 
# Use set comprehension.
# ---------------------------------------------------------
omega = {}
temp = 0
for i in range(1, 7):
    for j in range(1, 7):
        omega[(i, j)] = i + j
        if i + j > 10:
            temp +=1

result = temp/len(omega)
print(f"Probability {result}" )
