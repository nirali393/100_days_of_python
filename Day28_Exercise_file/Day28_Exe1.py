# -------------------Exercise 1----------------------------
# Write a program that reads playway.txt file containing Playway stock data, and then calculates the average closing price (3-day average).
# Print the result to the console as shown below.

# Expected result:
# 3-day average closing price: xxx.xx
# ----------------------------------------------------------

try:
    f = open("playway.txt", "r")
    print(f.read())
    f.readlines()
except FileNotFoundError:
    print("File not found")