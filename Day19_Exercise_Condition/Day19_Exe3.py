# -------------------Exercise 3----------------------------
# The following list is given:

# project_ids = ['02134', '24253']

# Check if the following project id:

# project_id = '02135'
# is in the project_ids list. If not, add this project_id to the list and print this list to the console.

# Expected result:
# ['02134', '24253', '02135']
# ---------------------------------------------------------

project_ids = ['02134', '24253']
project_id = '02135'

# if project_ids.count(project_id) == 0:
#     project_ids.append(project_id)
#     print(f'New record of {project_id} is append in list: {project_ids}')
# else: 
#     print(f'{project_id} is found in {project_ids}')

if not project_id in project_ids:
    project_ids.append(project_id)

print(project_ids)
