d = dict()
for i in input():
    d[i] = d.get(i, 0) + 1
print(d)
