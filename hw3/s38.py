d = dict()
s = input()
for i in s:
    d[i] = d.get(i, 0) + 1
print(max(d, key=d.get))
