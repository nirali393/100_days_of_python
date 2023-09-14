# -------------------Exercise 2 -------------------
# A list of tickers from the Dow Jones index is given:

# tickers = [
#     'AAPL.US',
#     'AXP.US',
#     'BA.US',
#     'CAT.US',
#     'CSCO.US',
#     'CVX.US',
#     'DIS.US',
#     'DOW.US',
#     'GS.US',
#     'HD.US',
#     'IBM.US',
#     'INTC.US',
# ]

# Transform this list into a list of two-element tuple objects (index, ticker) and print it to the console.
# Formatted result for better view:

# [(0, 'AAPL.US'),
#  (1, 'AXP.US'),
#  (2, 'BA.US'),
#  (3, 'CAT.US'),
#  (4, 'CSCO.US'),
#  (5, 'CVX.US'),
#  (6, 'DIS.US'),
#  (7, 'DOW.US'),
#  (8, 'GS.US'),
#  (9, 'HD.US'),
#  (10, 'IBM.US'),
#  (11, 'INTC.US')]

# Expected result:
# [(0, 'AAPL.US'), (1, 'AXP.US'), (2, 'BA.US'), (3, 'CAT.US'), (4, 'CSCO.US'), (5, 'CVX.US'), (6, 'DIS.US'), (7, 'DOW.US'), (8, 'GS.US'), (9, 'HD.US'), (10, 'IBM.US'), (11, 'INTC.US')]
# --------------------------------------------------------- 

tickers = [
    'AAPL.US',
    'AXP.US',
    'BA.US',
    'CAT.US',
    'CSCO.US',
    'CVX.US',
    'DIS.US',
    'DOW.US',
    'GS.US',
    'HD.US',
    'IBM.US',
    'INTC.US',
]
a = list(enumerate(tickers))

print(a)
