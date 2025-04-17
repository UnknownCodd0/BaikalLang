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
        if isinstance(other, Строка):
            return self.value == other.value

        elif isinstance(other, str):
            return self.value == other

        else:
            raise ValueError

#
# class Буль_Буль:
#     def __init__(self, value):
#         self.value = value
#
class Функции:
    @staticmethod
    def Вывести(arg):
        if arg in globals():
            print(globals()[arg].get_value())
        else:
            print(arg)

    #@staticmethod


    #@staticmethod
    #def ВывестиПеременную(var):
        #print(var)

    @staticmethod
    def Вид(arg):
        return type(arg)

    @staticmethod
    def Код_Змей(arg):
        eval(arg)

    @staticmethod
    def Если(att1, cond, att2, *args):
        if cond == "==":
            print("FFF")
            if att1 == att2:
                for i in range(0, len(args), 2):
                    args[i](args[i + 1])

            else:
                return

        elif cond == "~=":
            if att1 != att2:
                for i in range(0, len(args), 2):
                    args[i](args[i + 1])

            else:
                return
