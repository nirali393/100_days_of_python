# -------------------Exercise 1---------------------------- 
# Consider the problem of binary classification in machine learning. 
# We have the following y_true list with classes from the test set and the following y_pred list with classes provided by the model:

# y_true = [0, 0, 1, 1, 0, 1, 0]
# y_pred = [0, 0, 1, 0, 0, 1, 0]

# Our task is to implement a function called accuracy(), which takes two arguments y_true, y_pred and calculates the accuracy of our model. The result is rounded to four decimal places.
# In response, call the function on our data and print the result to the console.

# Expected result:
# 0.8571
# ---------------------------------------------------------

y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]

def accuracy(y_true, y_pred):
    counter = 0
    for i, j in zip(y_true, y_pred):
        if i == j:
            counter += 1
    return round(counter / len(y_true), 4)
 
 
print(accuracy(y_true, y_pred))
