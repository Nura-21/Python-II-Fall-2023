import pandas as pd

# Read the data from the output_11.csv file
data = pd.read_csv("input_11.csv", header=None, names=["x1", "x2", "y"])

# Function to calculate the predicted value for a set of inputs
def predict(x1, x2):
    # Replace this with your neural network prediction logic
    # For now, let's assume a simple linear model: y = w1*x1 + w2*x2 + b
    w1 = 0.5
    w2 = 0.3
    b = 0.2
    return w1*x1 + w2*x2 + b

# Calculate the mean squared error for each row in the dataset
data["predicted"] = data.apply(lambda row: predict(row["x1"], row["x2"]), axis=1)
data["error"] = (data["predicted"] - data["y"])**2

# Calculate the mean squared error (MSE)
mse = data["error"].mean()

print("Mean Squared Error (MSE):", mse)
