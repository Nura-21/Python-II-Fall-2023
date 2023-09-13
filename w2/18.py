list = []
for i in range(7):
    temp = []
    for j in range(5):
        if ((i == 0 or i == 6) and 0 < j < 4) or (i == 3 and j != 1) or (i == 2 and j == 0) or (i != 0 and i != 2 and i != 3 and i != 6 and (j == 0 or j == 4)):
            temp.append('*')
        else:
            temp.append(' ')
    list.append(temp)
for row in list:
    print(''.join(row))
