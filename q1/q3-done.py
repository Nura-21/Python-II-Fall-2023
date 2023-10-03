f_text, s_text = [], []
with open('q3-1.txt', 'r') as f:
    f_text = f.readlines()

with open('q3-2.txt', 'r') as f:
    s_text = f.readlines()

f_len, s_len = len(f_text), len(s_text)
# Expected
# 1-1
# 1-2
# 2-1
# 2-2
# 3-1
# 3-2
with open('q3-3.txt', 'w') as f:
    for i in range(max(f_len, s_len)):
        if i + 1 <= f_len:
            f.write(f_text[i])
        if i + 1 <= s_len:
            f.write(s_text[i])

# DONE
