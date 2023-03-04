lst = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]


s = []
for i in lst:
    s.extend(i.values())
    if len(s) == 5:
        f"{s[0]}, {s[1]}, {s[2]}, {s[3]}, и {s[4]}"
    if len(s) == 4:
        print(f"{s[0]}, {s[1]}, {s[2]}, и {s[3]}")
    if len(s) == 3:
        print(f"{s[0]}, {s[1]}, и {s[2]}")
    if len(s) == 2:
        print(f"{s[0]} и {s[1]}")
    if len(s) == 1:
        print(f"{s[0]}")
    if len(s) == 0:
         print(f"[]")

#
# # код ниже не стоит удалять, он нужен для проверки
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
# assert format_name_list([{'name': 'Bart'}]) == 'Bart'
# assert format_name_list([]) == ''
# assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
# assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
# assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
# print('Проверки пройдены')