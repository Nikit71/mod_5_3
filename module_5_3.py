#   Домашняя работа по уроку "Перегрузка операторов"
#   Задача "Нужно больше этажей":
print('\n')

class House:
    def __init__(self, name, number_of_floors):
        self.name = (name)                          #   имя
        self.number_of_floors =number_of_floors     #   кол - во этажей

    def __str__(self):
        return f"Название:  {self.name}  кол-во этажей: {str(self.number_of_floors)}"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):    # - должен возвращать True, если количество этажей одинаковое у self и у other.       (h1 == h2)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):    # - должен возвращать True, если  (<)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):    # - должен возвращать True, если  (<=)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):    # - должен возвращать True, если  (>)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):    # - должен возвращать True, если  (>=)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):    # - должен возвращать True, если  (!=)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):       # - должен возвращать self.number_of_floors + value
        if isinstance(value, int):
            return House(self.name,self.number_of_floors + value)
        else:
            return self

    def __radd__(self, value):      # - должен возвращать  += value
        return self.__add__(value)


    def __iadd__(self, value):      # - должен возвращать value + self.number_of_floors
        return self.__add__(value)
        pass

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10                        # __add__
print(h1)
print(h1 == h2)
h1 += 10                            # __iadd__
print(h1)
h2 = 10 + h2                        # __radd__
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)










