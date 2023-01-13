import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
w= list(map(lambda x: list(map(int, x.split())), lst_in))
sz = list(zip(*w))
random.shuffle(sz)
sz2= list(zip(*sz))
for i in sz2:
    print(*i)