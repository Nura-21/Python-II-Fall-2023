def get_fib(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
    return fib


print(list(map(lambda x: x ** 3, get_fib(int(input())))))
