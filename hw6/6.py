import re

for _ in range(int(input())):
    pair = input().strip()
    name, email = re.match(r'(.+?)\s<([^<>]+)>', pair).groups()
    if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', email):
        print(f"{name} <{email}>")
