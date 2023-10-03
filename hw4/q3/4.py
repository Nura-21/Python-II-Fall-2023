# Function to generate a list of prime numbers up to a given limit
def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

# Read the number of primes to print
num_primes = int(input())

# Read the indices of primes to print
indices = list(map(int, input().split()))

# Generate a list of prime numbers up to a sufficient limit
limit = max(indices) * 10  # Adjust the limit as needed
prime_list = generate_primes(limit)

# Print the prime numbers corresponding to the specified indices
result = [prime_list[index - 1] for index in indices]
print(" ".join(map(str, result)))
