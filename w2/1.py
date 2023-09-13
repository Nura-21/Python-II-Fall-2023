import random
for i in range(random.randrange(100, 5000)):
    if (i % 7 == 0 and i % 5 == 0):
        print(i, end=' ')
