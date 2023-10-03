# Function to calculate the area of a triangle given its vertices
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

# Read the number of triangles to process
num_triangles = int(input())

# Initialize a list to store the results
results = []

# Process each triangle
for _ in range(num_triangles):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
    results.append(area)

# Print the results separated by spaces
print(" ".join(map(lambda x: f"{x:.7f}", results)))
