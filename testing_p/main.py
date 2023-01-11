# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)
def fib_rec(N, f=[]):
    if len(f)<N:
        if len(f) < 2:
            f.append(1)
        else:
            f.append(f[-2] + f[-1])
        fib_rec(N, f)
        return f