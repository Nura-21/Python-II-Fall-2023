list = []
for i in range(7):
    temp = []
    for j in range(5):
        if ((i == 0 or i == 3) and (0 < j < 4)) or (((i != 0) and (j == 0 or j == 4))):
            temp.append('*')
        else:
            temp.append(' ')
    list.append(temp)
for row in list:
    print(''.join(row))
