list = []
for i in range(7):
    temp = []
    for j in range(5):
        if ((i == 0 or i == 6) and (j < 4)) or (0 < i < 6 and (j == 0 or j == 4)):
            temp.append('*')
        else:
            temp.append(' ')
    list.append(temp)
for row in list:
    print(''.join(row))
