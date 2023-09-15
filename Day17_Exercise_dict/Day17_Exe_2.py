# -------------------Exercise 2----------------------------
# The following dictionary is given:
# stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}

# Delete the 'traffic' key pair from this dictionary and print it to the console.

# Expected result:
# {'site': 'e-smartdata.org', 'type': 'organic'}
# ---------------------------------------------------------

stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}

del stats['traffic']
print(stats)
