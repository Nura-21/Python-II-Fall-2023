s = input()
print(
    *[f'Current char {s[i]} position at {i}' for i in range(len(s))], sep='\n')
