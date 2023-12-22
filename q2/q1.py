n = int(input())

l = []


def find_sum_rectangle(l):
    sum = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            sum += l[i][j]
    return sum


for i in range(n):
    row = [int(each) for each in input().split(' ')]
    l.append(row)

# Только не хватало алгоритма нахождения всех суб-ректанглов
