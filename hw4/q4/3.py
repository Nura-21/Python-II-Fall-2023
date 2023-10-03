# Function to find the maximum amount of candies using dynamic programming
def max_candies(isles):
    n = len(isles)
    dp = [0] * (n + 2)

    for i in range(n - 1, -1, -1):
        dp[i] = max(isles[i] + dp[i + 2], dp[i + 1])

    return dp[0]

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    isles = list(map(int, input().split()))
    result = max_candies(isles)
    print(result)
