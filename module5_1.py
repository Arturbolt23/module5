class House():
    def __init__(self, name ,number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor


    def to_go(self, new_floor):
        self.new_floor = new_floor
        if new_floor < 1 or new_floor > self.number_of_floor :
            print('такого этажа не существует!')
        else:
            for flor in range(1, new_floor + 1):
                print(flor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.to_go(5)
h2.to_go(10)

h3 = House('какой то новый', 25)
h3.to_go(14)
