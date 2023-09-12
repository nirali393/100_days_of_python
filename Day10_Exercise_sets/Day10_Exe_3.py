# -------------------Exercise 3-------------------
# We have two sets of customer IDs:
# ad1_id = {'001', '002', '003'}
# ad2_id = {'002', '003', '007'}

# Each set stores the id of the customers who made the purchase based on the specific ad. We have two ads. Each customer can use the offer only twice in campaign. Choose the ID of the customers to whom you can send another ad (or ids that only appeared once in both sets).

# Expected result: Selected ID: { '007', '001'}
# Note: Remember that the set is an unordered data structure. You may get a different order of items than the expected result. You don't have to worry about it.
# --------------------------------------------------

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}

print(f'Selected ID: {ad1_id.symmetric_difference(ad2_id)}')
