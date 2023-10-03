from math import sqrt


def find_len_between(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


res = []
for i in range(int(input())):
    lens = [int(i) for i in input().split()]
    x1, y1, x2, y2, x3, y3 = lens[0], lens[1], lens[2], lens[3], lens[4], lens[5]
    a = find_len_between(x1, y1, x2, y2)
    b = find_len_between(x2, y2, x3, y3)
    c = find_len_between(x1, y1, x3, y3)
    # forgot formula of area triangle
