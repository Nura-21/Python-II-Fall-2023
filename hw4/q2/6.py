roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

# Create a copy of the list to avoid modifying it while iterating
roll_number_copy = roll_number.copy()

# Iterate through the list and check if each element is in the dictionary
for number in roll_number_copy:
    if number not in sample_dict.values():
        roll_number.remove(number)

print("After removing unwanted elements from list:", roll_number)
