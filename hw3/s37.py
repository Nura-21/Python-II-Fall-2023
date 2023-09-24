d = dict()
s = input()
for word in s.split(' '):
    d[word] = d.get(word, 0) + 1
d.pop(max(d, key=d.get))
print(max(d, key=d.get))
