# Define the first and second lists
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# Extract elements at odd indices from list one
odd_elements_l1 = l1[1::2]

# Extract elements at even indices from list two
even_elements_l2 = l2[::2]

# Create the third list by concatenating the two extracted lists
third_list = odd_elements_l1 + even_elements_l2

# Print the results
print("Element at odd-index positions from list one:", odd_elements_l1)
print("Element at even-index positions from list two:", even_elements_l2)
print("Printing Final third list:", third_list)
