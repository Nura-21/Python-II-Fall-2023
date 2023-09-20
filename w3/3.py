age = int(input("In human: "))
if 0 <= age <= 2:
    res = age * 10.5
else:
    res = 21 + (age - 2) * 4
print("In dog: ", res)
