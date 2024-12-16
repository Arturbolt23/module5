'''

'''
class House():

    houses_history = []

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
    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f'Название : {self.name}, количество этажей : {self.number_of_floor} ')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        return False

    def get_value(self):
        value = int(input('введите количествуо этажей которое хотите добавить :'))
        return value

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floor += other
            return self
        elif isinstance(other, House):
            value = self.get_value()
            self.number_of_floor += value
            return self
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)


    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __del__(self):
        print ( f'{self.name} снесен, но останется с нами навсегда в памяти :-((')

h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)



# Удаление объектов

del h2

del h3



print(House.houses_history)
