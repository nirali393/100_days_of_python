
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
    # print(content)
    temp_var = 0
    dict_value = {}

    for line in content[1:]:
        values = line.split(',')
        dict_value.update({int(values[5]) : values[0]})
        

max_key = max(dict_value.keys())
print(f"Date for higest volue: {dict_value.get(max_key)}")
