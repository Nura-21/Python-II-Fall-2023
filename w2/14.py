answer = []
for i in range(100, 400):
    if (int(str(i)[0]) % 2 == 0) and (int(str(i)[1]) % 2 == 0) and (int(str(i)[2]) % 2 == 0):
        answer.append(str(i))
print(",".join(answer))
