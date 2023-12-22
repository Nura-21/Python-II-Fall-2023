import numpy as np
import pandas as pd

# Read input parameters from input_7.csv
input_data = pd.read_csv('input_7.csv', header=None)
m, thetaZero, thetaOne, lamda = input_data.iloc[0]

# Extract x and y values
xy_values = input_data.iloc[1:].values
x = xy_values[:, 0]
y = xy_values[:, 1]

# Calculate the cost function for linear regression with regularization
cost = (np.sum((x * thetaOne + thetaZero - y)**2) + lamda * (thetaZero**2 + thetaOne**2)) / (2 * m)

# Write the result to output_7.csv
output_data = pd.DataFrame([cost], columns=['Cost'])
output_data.to_csv('output_7.csv', index=False)
