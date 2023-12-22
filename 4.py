import csv

def normalize_features(m, x):
    # Calculate mean and standard deviation for each feature
    means = [sum(col) / m for col in zip(*x)]
    std_devs = [(sum((xi - means[i]) ** 2 for xi in col) / m) ** 0.5 for i, col in enumerate(zip(*x))]

    # Normalize the features
    normalized_x = [
        [round((xi - means[i]) / std_devs[i], 2) for i, xi in enumerate(row)]
        for row in x
    ]

    return normalized_x

def main():
    # Read input from input_4.csv
    with open('input_4.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        m = int(next(reader)[0])
        x = [list(map(float, row)) for row in reader]

    # Normalize the features
    normalized_x = normalize_features(m, x)

    # Write output to output_4.csv
    with open('output_4.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in normalized_x:
            writer.writerow(row)

if __name__ == "__main__":
    main()
