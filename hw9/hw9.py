def matrix_multiply(matrix1, matrix2):
    result = []

    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            dot_product = 0
            for k in range(len(matrix2)):
                dot_product += matrix1[i][k] * matrix2[k][j]
            row.append(dot_product)
        result.append(row)

    return result

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

matrix_a = input_matrix()
matrix_b = input_matrix()

result = matrix_multiply(matrix_a, matrix_b)

print("Result:")
for row in result:
    print(row)
