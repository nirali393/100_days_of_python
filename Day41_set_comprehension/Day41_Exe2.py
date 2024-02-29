# -------------------Exercise 2---------------------------- 
# The following text is given:
# desc = "Playway: Playway is a producer of computer games."

# Change all characters to lowercase, remove the colon, period and then split the text into words.

# Create a set of unique words and print the length of this set to the console.
# ---------------------------------------------------------

desc = "Playway: Playway is a producer of computer games."
words = desc.lower().replace(':','').replace('.','').split(' ')
print(len(set(words)))

