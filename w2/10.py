lines = []
while True:
    text = input()
    if len(text) == 0:
        break
    else:
        lines.append(text.lower())
for text in lines:
    print(text)
