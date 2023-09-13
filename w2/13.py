import re
password = input()
if (re.search('[a-z]', password) != None and re.search('[A-Z]', password) != None and re.search('[0-9]', password) and re.search('[$#@]', password) and len(password) >= 6 and len(password) <= 16):
    print('Valid')
else:
    print('Not valid')
