def get_sort(d):
    s ={i:j for i,j in sorted(d.items(), reverse=True)}
    return list(s.values())


d2=get_sort({'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'})
print(d2)