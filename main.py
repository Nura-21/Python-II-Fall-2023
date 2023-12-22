import csv
import numpy as np

# Read input data from the input CSV file
input_filename = "input_5.csv"
output_filename = "output_5.csv"

m = 0
max = 0
ind = 0
result = []

# Read data from the input file
with open(input_filename, "r") as input_file:
    max = len(input_file.readlines())

# Read data from the input file
with open(input_filename, "r") as input_file:
    reader = csv.reader(input_file)
    while ind < max:
        data = []
        m = int(next(reader)[0])
        ind += 1
        for _ in range(m):
            x0, x1, h_theta_x = map(float, next(reader))
            data.append((x0, x1, h_theta_x))

        # Convert data into NumPy arrays for easier calculations
        data = np.array(data)
        X = data[:, :2]
        y = data[:, 2]

        # Calculate theta0 and theta1 using the normal equations
        X_transpose = X.T
        theta = np.linalg.inv(X_transpose @ X) @ X_transpose @ y

        theta0, theta1 = theta[0], theta[1]
        result.append(f"{theta0:.2f},{theta1:.2f}\n")

        ind += m
        print(ind)

print(result)



# Write the results to the output file
with open(output_filename, "w") as output_file:
    for res in result:
        output_file.write(res)

# print(f"theta0: {theta0:.2f}")
# print(f"theta1: {theta1:.2f}")
