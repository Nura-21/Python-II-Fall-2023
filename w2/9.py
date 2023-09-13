n, m = int(input('Row: ')), int(input('Col: '))
list = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(i * j)
    list.append(temp)
print(list)
