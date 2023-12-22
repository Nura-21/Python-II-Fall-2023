import numpy as np
import pandas as pd

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def feedforward(input_file, output_file):
    # Load input data
    input_data = pd.read_csv(input_file, header=None).values

    # Neural network parameters (adjusted weights and biases)
    weights_hidden = np.array([[0.6, -0.5], [0.2, 0.8]])
    bias_hidden = np.array([0.1, 0.4])

    weights_output = np.array([[0.4, 0.1], [-0.2, 0.6]])
    bias_output = np.array([0.1, -0.2])

    # Perform feedforward operation
    hidden_layer_input = np.dot(input_data, weights_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_output) + bias_output
    output_layer_output = sigmoid(output_layer_input)

    # Write the output to a CSV file
    pd.DataFrame(output_layer_output).to_csv(output_file, header=False, index=False)

# Use the provided input data
feedforward("input_10.csv", "output_10.csv")
