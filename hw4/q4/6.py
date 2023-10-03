# Function to classify a triangle as right, acute, or obtuse
def classify_triangle(a, b, c):
    # Check if it's a right triangle
    if a ** 2 + b ** 2 == c ** 2:
        return "R"
    # Check if it's an acute triangle
    elif a ** 2 + b ** 2 > c ** 2:
        return "A"
    # It's an obtuse triangle
    else:
        return "O"

# Read the number of triangles
num_triangles = int(input())

# Process each triangle and classify it
results = []
for _ in range(num_triangles):
    sides = list(map(int, input().split()))
    result = classify_triangle(*sides)
    results.append(result)

# Print the results separated by spaces
print(" ".join(results))
