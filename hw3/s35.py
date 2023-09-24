d = dict()
s = input()
for i in s:
    if i not in d:
        d[i] = 1
    else:
        print(i)
        break
