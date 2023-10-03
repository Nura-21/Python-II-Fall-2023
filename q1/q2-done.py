def find_seq(n, cnt):
    if (n <= 1):
        return cnt
    cnt += 1
    return find_seq(n / 2 if n % 2 == 0 else (n * 3 + 1), cnt)


for i in range(int(input())):
    print(find_seq(int(input()), 0))
