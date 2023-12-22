import re
x, y = [int(each) for each in input().split(' ')]


def normalize_text(s):
    return f'{str(s)[0].upper()}{str(s)[1:].lower()}'


t = []

for i in range(x):
    row = [each for each in input().split(' ')]
    t.append([row[j] if len(row) > j else ' ' for j in range(y)])

col = 0
text = ''
while col < y:
    row = 0
    while row < x:
        text += t[row][col]
        row += 1
    col += 1

for word in re.findall(r'[A-Za-z0-9]+', text):
    print(normalize_text(word), end=' ')
