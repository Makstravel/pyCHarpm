class Building:

    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.floors = [None] * num_floors

    def __setitem__(self, floor, company):
        if self.floors[floor] is not None:
            print(f"Floor {floor} is already occupied by {self.floors[floor]}. Replacing with {company}.")
        self.floors[floor] = company

    def __getitem__(self, item):
        return self.floors[item]


    def __delitem__(self, floor):
        self.floors[floor] = None


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
