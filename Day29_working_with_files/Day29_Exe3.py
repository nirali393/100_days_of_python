# -------------------Exercise 3----------------------------
# Generate all even numbers from 2 to 18 inclusive. 
# Then write each number on a separate line to the file called num.txt.
# ---------------------------------------------------------

with open("num.txt","w") as file:

    for i in range(2,19):
        if i %2 ==0:
            file.write(f"{str(i)}\n")
            