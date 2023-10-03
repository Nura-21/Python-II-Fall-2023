# Function to calculate the sum of the first N terms of an arithmetic sequence
def arithmetic_sequence_sum(A, B, N):
    return N * (2 * A + (N - 1) * B) // 2

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    A, B, N = map(int, input().split())
    result = arithmetic_sequence_sum(A, B, N)
    print(result, end=" ")

# Print a newline character to separate test cases
print()
