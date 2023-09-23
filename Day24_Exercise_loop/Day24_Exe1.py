# -------------------Exercise 1----------------------------
# A dictionary of companies from the WIG.GAMES index is given. The key is the 3-letter company ticker and value - close price:
# gaming = {
#     '11B': 362.5,
#     'CDR': 297.0,
#     'CIG': 0.85,
#     'PLW': 318.0,
#     'TEN': 300.0
# }
# Iterate through this dictionary and print the tickers of those companies where closing price is greater than 100.00 PLN.
# Expected result:
# 11B
# CDR
# PLW
# TEN
# -----------------------------------------------------------

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for key , value in gaming.items():
    if value > 100:
        print(key)