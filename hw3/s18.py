s = input()
num_upper = 0
for letter in s[:4]:
    if letter.upper() == letter:
        num_upper += 1
if num_upper >= 2:
    print(s.upper())
else:
    print(s)
