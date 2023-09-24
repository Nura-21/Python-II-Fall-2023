d = dict()
for word in input().split(' '):
    d[word] = d.get(word, 0) + 1
print(d)
