import re
email = 'example@example.com'

if re.search(r'@.*\.', email):
    print('y')
else:
    print('n')