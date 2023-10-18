# -------------------Exercise 1----------------------------
# Write a program that reads playway.txt file containing Playway stock data, and then calculates the average closing price (3-day average).
# Print the result to the console as shown below.

# Expected result:
# 3-day average closing price: xxx.xx
# ----------------------------------------------------------


import pandas as pd

try:
    with open("playway.txt", "r") as f:
        first_line = True
        temp_value = 0
        for line in f:
            if first_line:
                first_line = False
                continue
            values = line.split(',')
            value_at_index_4 = values[4]
            temp_value = temp_value + int(value_at_index_4)

        reault = int(temp_value)/3
        print(f'3-day average closing price:{reault:.2f}')
            

except FileNotFoundError:
    print("File not found")
    