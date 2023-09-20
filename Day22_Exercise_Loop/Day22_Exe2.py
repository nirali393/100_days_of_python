# -------------------Exercise 2----------------------------
# Write a program that returns a list of values above the given threshold = 0.5 from the following list:

# probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

# Expected result:
# [0.91, 0.55, 0.76]
# ----------------------------------------------------------

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
threshold = 0.5
above_threshold_probabilities = []
for i in probabilities:
    if i > threshold:
        above_threshold_probabilities.append(i)
print(above_threshold_probabilities)
