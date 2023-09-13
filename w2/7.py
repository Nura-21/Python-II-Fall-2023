first, second = 0, 1
r_range = int(input('Right range: '))
print(first, end=' ')
while second < r_range:
    print(second, end=' ')
    first, second = second, first + second
