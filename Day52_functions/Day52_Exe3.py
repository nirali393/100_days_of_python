# -------------------Exercise 1---------------------------- 
# MSE - Mean Squared Error is a function that allows you to check the accuracy of the machine learning model. MSE is popular in regression models.
# For any:

# MSE can be calculated by the following formula:

# Example:
# [IN]: y_true = [10, 10.5, 11.2, 10.4]
# [IN]: y_pred = [10.2, 10.4, 10.8, 11.0]
# [IN]: mse(y_true, y_pred)   
# [OUT]: 0.142
# Implement a function called mse(). Round the result to three decimal places.
# Note: You only need to implement this function.
# ---------------------------------------------------------

def mse(y_true, y_pred):
    return round(
        sum([(i[1] - i[0]) ** 2 for i in zip(y_true, y_pred)])
        / len(y_true),
        3,
    )

y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]

result = mse(y_true, y_pred)
print(result)