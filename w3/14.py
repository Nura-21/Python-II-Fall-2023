cnt, sum = 0, 0
n = int(input())
while n != 0:
    n = int(input())
    sum += n
    cnt += 1

print('Average: ', sum / (cnt - 1))
print('Sum: ', sum)
