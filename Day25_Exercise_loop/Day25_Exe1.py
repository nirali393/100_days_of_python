# -------------------Exercise 1----------------------------
# The following list of hashtags is given:

# hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
# Check if all objects in the list are of str type. If so, print True, otherwise print False. Use the break statement in your solution.
# Expected result:False
# ---------------------------------------------------------

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

result = True

for i in hashtags:
    if not isinstance(i, str):
        result = False
        break

print(result)