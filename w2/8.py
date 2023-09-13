import random
for i in range(random.randrange(1, 50)):
    if (i % 3 == 0):
        print('Mkm', end='')
    if (i % 5 == 0):
        print('KBTU', end='')
    if (i % 3 != 0 and i % 5 != 0):
        print(i, end='')
    print()
