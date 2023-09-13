text = 'KBTU MKM 2018'
let_cnt, dig_cnt = 0, 0
for i in text:
    if (i.isalpha()):
        let_cnt += 1
    if (i.isdigit()):
        dig_cnt += 1
print('Letters:', let_cnt)
print('Digits:', dig_cnt)
