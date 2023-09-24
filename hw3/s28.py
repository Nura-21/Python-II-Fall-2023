d = dict()
s = input()
for i in s:
    d[i] = d.get(i, 0) + 1
print(*[f'{k} : {v}\n' if v > 1 else '' for k, v in d.items()])
