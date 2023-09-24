s = input()
snot = s.find('not')
spoor = s.find('poor')
if spoor > snot and snot > 0 and spoor > 0:
    s = s.replace(s[snot:(spoor+4)], 'good')
    print(s)
else:
    print(s)
