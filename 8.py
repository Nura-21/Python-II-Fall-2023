import numpy as np
import pandas as pd

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def calculate_cost(theta, X, y, lambda_reg):
    m = len(y)
    h = sigmoid(X @ theta)
    
    # Cost function without regularization
    J = (-1/m) * (y.T @ np.log(h) + (1 - y).T @ np.log(1 - h))
    
    # Regularization term
    reg_term = (lambda_reg / (2 * m)) * np.sum(theta[1:]**2)
    
    # Add regularization to the cost function
    J = J + reg_term
    
    return J

def main():
    # Read input from the file
    with open('input_8.csv', 'r') as file:
        lines = file.readlines()
        m, thetaZero, thetaOne, lamda = map(float, lines[0].strip().split(','))
        data = [list(map(float, line.strip().split(','))) for line in lines[1:]]
    
    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Separate X and y
    y = df.iloc[:, -1].values
    X = df.iloc[:, :-1].apply(lambda col: col.fillna(0)).values
    
    # Add intercept term to X
    X = np.insert(X, 0, 1, axis=1)
    
    # Initialize theta with the correct length
    theta = np.zeros(X.shape[1])
    
    # Calculate and print the cost function
    cost = calculate_cost(theta, X, y, lamda)
    print(f"{cost:.2f}")

    # Save output to file
    output_df = pd.DataFrame([cost])
    output_df.to_csv('output_8.csv', header=False, index=False)

if __name__ == "__main__":
    main()
