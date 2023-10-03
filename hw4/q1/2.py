list = [123, 456, 6, 68, 234, 867, 86, 56]
f = list[0]
for i in range(len(list) - 1):
    list[i] = list[i + 1]

list[-1] = f

print(list)
