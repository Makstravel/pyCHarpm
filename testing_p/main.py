import pickle


try:
    with open("test2.txt", 'w') as file:
        file.write(input())

except:
    print('Невозможно открыть файл')


