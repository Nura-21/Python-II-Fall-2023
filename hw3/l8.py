arr = [1, 1, 2, 2, 3, 3]


def no_dupl_arr(l):
    y = []
    for i in l:
        if i not in y:
            y.append(i)
    return y


def no_dupl(l):
    return list(set(l))


print(no_dupl_arr(arr))
print(no_dupl(arr))
