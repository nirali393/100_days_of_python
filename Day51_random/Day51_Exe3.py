# -------------------Exercise 2---------------------------- 
# Using the json package, dump the following dictionary:

# stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
# to the string, sorted by keys with indent 4. Print the result to the console.

# Expected result:
# {
#     "CDR": 329.0,
#     "PLW": 360.0,
#     "TEN": 320.0
# }
# ---------------------------------------------------------

import json


stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
result = json.dumps(stocks, sort_keys=True, indent=4)
 

print(result)