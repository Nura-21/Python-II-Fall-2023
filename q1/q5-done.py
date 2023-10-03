l = [int(i) for i in input().split()]
res = []
for i in range(1, len(l)):
    if l[i] < l[i - 1]:
        res.append(i - 1)
print(res)
