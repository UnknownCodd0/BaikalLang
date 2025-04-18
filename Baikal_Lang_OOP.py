class Runner:
    def __init__(self, value):
        self.value = value
    def run(self):
        pass

file = open(r"C:\Users\Tagir\Desktop\code.txt")

#for i in file:
    #print(file.readline())

class Строка:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def длина(self):
        return len(self.value)

    def маленькие_буквы(self):
        return self.value.lower()

    def срезы(self, arg1, arg2, arg3):
        return self.value[arg1:arg2:arg3]

    def большие_буквы(self):
        return self.value.upper()

    def сортировать(self):
        return self.value.sort()

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Переменная {self.name} со значением {self.value}"
#
class Число:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def Ноль_Один(self):
        return bin(self.value)

    def Модуль(self):
        return abs(self.value)

    def __add__(self, other):
        if isinstance(other, Число):
            return self.value + other.value

        elif isinstance(other, int):
            return self.value + other

        else:
            raise ValueError

    def __str__(self):
        return f"Переменная {self.name} со значением {self.value}"

    def __eq__(self, other):
        if isinstance(other, Число):
            return self.value == other.value

        elif isinstance(other, int):
            return self.value == other

        else:
            raise ValueError

    def __ne__(self, other):
        if isinstance(other, Число):
            return self.value != other.value

        elif isinstance(other, int):
            return self.value != other

        else:
            raise ValueError

    def __lt__(self, other):
        if isinstance(other, Число):
            return self.value < other.value

        elif isinstance(other, int):
            return self.value < other

        else:
            raise ValueError

    def __le__(self, other):
        if isinstance(other, Число):
            return self.value <= other.value

        elif isinstance(other, int):
            return self.value <= other

        else:
            raise ValueError

    def __gt__(self, other):
        if isinstance(other, Число):
            return self.value > other.value

        elif isinstance(other, int):
            return self.value > other

        else:
            raise ValueError

    def __ge__(self, other):
        if isinstance(other, Число):
            return self.value >= other.value

        elif isinstance(other, int):
            return self.value >= other

        else:
            raise ValueError

class ОбъявитьДругое:
    def __init__(self, name, value):
        self.value = value
        self.name = name



#
class Список:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def Сортировать(self, isreversed):
        if isreversed:
            return self.value.sort(reversed=True)

        else:
            return sorted(self.value)

    def Добавить(self, arg):
        self.value.append(arg)
        return self.value

    def Удалить(self, arg):
        del self.value[arg]
        return self.value

    def Найти(self, arg):
        return self.value.find(arg)

    def __eq__(self, other):
        if isinstance(other, Список):
            return self.value == other.value

        elif isinstance(other, list):
            return self.value == other

        else:
            raise ValueError(f"Невозможно сравнение Списка с {type(other)}")

#
class ЛогТип:
    def __init__(self, name, russian_value):
        self.name = name
        self.russian_value = russian_value

        if self.russian_value == "Правда":
            self.factical_value = True

        elif self.russian_value == "Ложь":
            self.factical_value = False

        else:
            raise Exception(f"Неправильное значение переменной: {name} со значением {self.russian_value}. ЛогТип принимает значения: Правда; Ложь")


    def __eq__(self, other):
        if isinstance(other, bool):
            return self.factical_value == other

        elif isinstance(other, ЛогТип):
            return self.factical_value == other.factical_value


class Функции:
    @staticmethod
    def Вывести(arg):
        if arg in globals():
            print(globals()[arg].get_value())
        else:
            print(arg)

    @staticmethod
    def Вид(arg):
        return type(arg)

