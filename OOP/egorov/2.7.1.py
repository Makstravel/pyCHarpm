class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for i, j in enumerate(self._notes, start=1):
            print(f'{i}. {j}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list