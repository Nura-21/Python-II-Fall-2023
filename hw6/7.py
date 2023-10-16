import re

for _ in range(int(input())):
    card_number = input().strip()
    print("Valid" if re.match(r'^[4-6]\d{3}[-]?\d{4}[-]?\d{4}[-]?\d{4}$', card_number)
          and not re.search(r'(\d)(-?\1){3,}', card_number) else "Invalid")
