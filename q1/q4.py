def create_primes(r):
    result = []
    for i in range(2, r + 1):
        div_cnt = 0
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                div_cnt += 1
        if div_cnt == 0:
            result.append(i)
    return result


n = int(input())
ind = [int(i) for i in input().split()]
primes = create_primes(max(ind))
print(len(primes), primes)
for i in ind:
    print(i)
