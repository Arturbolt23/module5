'''
Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты
сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:
Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.

Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.

Пример результата выполнения программы:
Пример выполняемого кода:

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
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



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__