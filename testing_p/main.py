try:
    with open("test2.txt", 'w', encoding='utf-8') as file:
        file.write(input(end='\n'))
except:
    print('Невозможно открыть файл')
