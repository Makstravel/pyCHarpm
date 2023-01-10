def counter_add(k):
    def plus_value():
        return k+5

    return plus_value

cnt= counter_add()
k = int(input())
print(cnt())

