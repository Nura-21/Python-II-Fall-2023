import re

for _ in range(int(input())):
    print("YES" if re.match(
        r'^(\+7|870)\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}$', input().strip()) else "NO")
