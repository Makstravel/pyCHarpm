n = list(map(int, input().split()))
def get_rec_sum(n):
    '''Функция вычисления суммы списка'''
    if len(n) ==1: #проверяем длинну списка
        return n[0]
    else:
        return n[0] + get_rec_sum(n[1:])  # извлекаем первое значение из списка и к нему плюсуем оставшийся список


