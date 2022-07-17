class Soda:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name

    def show_my_drink(self):
        print(f"Carbonated and {self.name}")

class TriangleChecker:
    def __init__(self, Object):
        self.sides = Object

    def check(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'




class KgToFund:
    def __init__(self, kg):
        self.__Pounds = None
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            print(f"Некорректный тип {type(kg)}")

    def to_pounds(self):
        self.__Pounds = self.__kg * 2, 2

    def set_kg(self, newKg):
        if isinstance(newKg, (int, float)):
            self.__kg = newKg
        else:
            return f'wrong type {type(newKg)}'

    def get_kg(self):
        return self.__kg

    def get_Pounds(self):
        if self.__Pounds:
            return self.__Pounds


class RealString:
    def __init__(self,some_text):
        self.__some_text = str(some_text)

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_str) == len(other.some_str)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_str) < len(other.some_str)

    def __le__(self, other):
        return self == other or self < other


class Student:
    def __init__(self, name='Niko', age=18, groupNumber='12b'):
        self.__name = name
        self.__age = age
        self.__groupNumber = groupNumber

    def getName(self):
        print(self.__name)

    def getAge(self):
        print(self.__age)

    def getGroupNumber(self):
        print(self.__groupNumber)

    def setNameAge(self, newAge):
        if isinstance(newAge, int):
            self.__age = newAge

    def setGroupNumber(self, NewGroup):
        self.__groupNumber = str(NewGroup)

# color(цвет), type(тип), year(год)
class Car:
    def __init__(self, name, typeOfAuto, year, color):
        self.__name = name
        self.__type = typeOfAuto
        self.__year = year
        self.__color = color

    def StartAuto(self):
        print(f"{self.__name} has been started!")

    def StopAuto(self):
        print(f"{self.__name} has beem stopped!")

    def RenameAuto(self, new__year):
        if isinstance(new__year, int):
            self.__year = new__year
            print(f"Changed since {new__year}!")

    def ToChangleTypeAuto(self, new__type):
        if isinstance(new__type, str):
            self.__year = new__type
            print(f"Changed for type {new__type}!")

    def toChangeColorAuto(self, new__color):
        if isinstance(new__color, str):
            self.__year = new__color
            print(f"Changed for color {new__color}!")
