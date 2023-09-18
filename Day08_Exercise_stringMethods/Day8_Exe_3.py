# -------------------Exercise 3-------------------
# The following variable is given: num = 3415

# Using the appropriate method for an object of type str, print the variable num preceded by four zeros to the console as shown below.
# Expected result: 00003415
# --------------------------------------------------

num = 3415

#zfill() require a string, num = 3415 is integer
x = str(num)
#zfill() will fill 0s in the string.
print(x.zfill(8))
