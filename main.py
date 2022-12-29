try:
    f = open("test.txt", 'w')
    r = f.read(1)
    f.close()

except FileNotFoundError:
    print('Невозможно открыть файл')
finally:
    print(f.closed)