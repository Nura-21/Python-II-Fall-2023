s = input()
res = []
for word in s.split(' '):
    res.append(word[0].upper() + word[1:len(word) - 1] + word[-1:][0].upper())
print(res)
