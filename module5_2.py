'''
Необходимо дополнить класс House следующими специальными методами:

__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
Пример результата выполнения программы:

Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20
'''
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
    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f'Название : {self.name}, количество этажей : {self.number_of_floor} ')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))