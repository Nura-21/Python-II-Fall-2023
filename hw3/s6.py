s = input()
try:
    if len(s) >= 2:
        if s[-3:] == 'ing':
            s += 'ly'
        else:
            s += 'ing'
    else:
        raise Exception()
    print(s)
except Exception:
    print('Less than 2')
