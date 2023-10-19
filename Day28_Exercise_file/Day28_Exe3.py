# # -------------------Exercise 2----------------------------
# The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:

# with open('playway.csv', 'r') as file:
#     content = file.read().splitlines()
# # ----------------------------------------------------------

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
    date = []
    close = []

    for line in content:  # Skip the header line (index 0)
        date.append(line.split(',')[0])  # Split the line by commas and extract the date
        close.append(line.split(',')[4])  # Split the line by commas and extract the date
        data_dict = {'Date': date,
                     'Close': close}
    print(data_dict , data_dict)
