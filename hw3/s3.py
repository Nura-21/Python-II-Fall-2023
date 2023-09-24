s = input()
res = ''
if len(s) >= 2:
    res = s[0:2] + s[-2:]
print(res)
