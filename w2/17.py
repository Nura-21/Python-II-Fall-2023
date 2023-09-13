list = []
for i in range(7):
    temp = []
    for j in range(5):
        if (i == 0 or i == 6) or (i == 3 and j < 4) or (j == 0 and 0 < i < 6):
            temp.append('*')
        else:
            temp.append(' ')
    list.append(temp)
for row in list:
    print(''.join(row))
