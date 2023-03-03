

try:
    def func(phrase):
        func(phrase)
    func('Это рекурсия, детка!')
except RecursionError:
    print('Кто-то должен остановить это безумие')






