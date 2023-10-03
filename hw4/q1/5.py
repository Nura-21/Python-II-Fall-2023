# Function to calculate the linear equation constants (a, b)
def calculate_linear_equation(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return (a, b)

# Read the number of test cases
num_test_cases = int(input())

# Initialize a list to store the results
results = []

# Process each test case
for _ in range(num_test_cases):
    x1, y1, x2, y2 = map(int, input().split())
    a, b = calculate_linear_equation(x1, y1, x2, y2)
    results.append((a, b))

# Print the results in the specified format
for result in results:
    print(f"({int(result[0])} {int(result[1])})", end=" ")

# Print a newline character to separate from the next line
print()
