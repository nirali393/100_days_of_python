
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
    # print(content)
    temp_var = 0

    for i,j in content[1:]:
        sep_str = int(i.split(',')[5])
        date = j.split(',')[0]
        # print(sep_str)

        if sep_str> temp_var:
            temp_var = sep_str
            
            
        else:
            continue

print(temp_var)

