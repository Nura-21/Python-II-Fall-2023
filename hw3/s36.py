d = dict()
s = input()
for word in s.split(' '):
    if word not in d:
        d[word] = 1
    else:
        print(word)
        break
