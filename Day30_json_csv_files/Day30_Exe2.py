# -------------------Exercise 2----------------------------
# Two following lists are given:

# headers = ['user_id', 'amount']
# users = [['001', '1400'], ['004', '1300'], ['007', '900']]

# Save the above data to the users.csv file (file in csv format - comma-separated values) as shown below.
# ---------------------------------------------------------
import csv


headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open("users.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(users)
    