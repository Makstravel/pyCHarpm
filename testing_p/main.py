def double_it(func):
    def doubl(*args, **kwargs):
        func(*args, **kwargs)

    return doubl*doubl