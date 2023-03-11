class Model:

    def __init__(self):
        self.value = None

    def query(self, **kwargs):
        self.value = kwargs

    def __str__(self):
        if self.value == None:
            return f'Model'
        else:
            return 'Model: ' + ', '.join([f'{key} = {value}' for key, value in self.value.items()])
