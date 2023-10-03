# Read the size of the array
array_size = int(input())

# Read the array values as integers
array_values = list(map(int, input().split()))

# Create a list of tuples where each tuple contains the original value and its index
array_with_indices = [(value, index + 1) for index, value in enumerate(array_values)]

# Sort the list of tuples based on the values
sorted_array_with_indices = sorted(array_with_indices)

# Extract the initial indexes from the sorted list
initial_indexes = [index for _, index in sorted_array_with_indices]

# Print the initial indexes as space-separated integers
print(" ".join(map(str, initial_indexes)))
