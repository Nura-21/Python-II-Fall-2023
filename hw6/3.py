import re
valid_emails = []

for _ in range(int(input())):
    email = input().strip()
    if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', email):
        valid_emails.append(email)

print(valid_emails)
