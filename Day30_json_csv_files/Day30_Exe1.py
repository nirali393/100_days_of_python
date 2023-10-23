# -------------------Exercise 1----------------------------
# The following dictionary:
# stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
# save to stocks.json using the json package. Set the indent to 4.
# ---------------------------------------------------------

import json


stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open("stocks.json", "w") as file:
    file.write(json.dumps(stocks, indent = 4))