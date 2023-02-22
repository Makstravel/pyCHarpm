emal = input()
s = emal.find('@')
if '.' in emal[s:]:
    print('Yes')
else:
    raise ValueError('введите верный логин')