def double_it(func):
    def doubl(*args, **kwargs):
        s= func(*args, **kwargs)
        return s+s

    return doubl