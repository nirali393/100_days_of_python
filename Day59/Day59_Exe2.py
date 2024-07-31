# -------------------Exercise 2---------------------------- 
# Using the built-in datetime module and the datetime.datetime.strptime() function, parse the following str objects:
# date_str_1 = '3 March 1995'
# date_str_2 = '3/9/1995'
# date_str_3 = '21-07-2021'
# to datetime objects. Print the result to the console.

# Tip:
# >>> help(datetime.datetime.strptime)
 
# Help on built-in function strptime:
# strptime(...) method of builtins.type instance
#     string, format -> new datetime parsed from a string (like time.strptime()).

# Expected result:
# 1995-03-03 00:00:00
# 1995-09-03 00:00:00
# 2021-07-21 00:00:00
# ---------------------------------------------------------

from datetime import datetime
 
 
date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'
 
dt1 = datetime.strptime(date_str_1, '%d %B %Y')
dt2 = datetime.strptime(date_str_2, '%d/%m/%Y')
dt3 = datetime.strptime(date_str_3, '%d-%m-%Y')
 
 
print(dt1)
print(dt2)
print(dt3)