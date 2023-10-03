# Function to calculate the number of steps to reach 1 in the Collatz sequence
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Read the number of test cases
num_test_cases = int(input())

# Read the test cases as a list of integers
test_cases = list(map(int, input().split()))

# Calculate and print the number of steps for each test case
results = [collatz_steps(x) for x in test_cases]
print(" ".join(map(str, results)))
