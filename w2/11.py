for i in [n for n in input().split(',')]:
    if not int(i, 2) % 5:
        print(i)
