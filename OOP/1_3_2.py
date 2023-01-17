class Config:
    pass


def create_instance(n: int) -> Config:
    obj = Config()
    for i in range(1, n+1):
        setattr(obj, f'attribute{i}', f'value{i}')
    return obj
