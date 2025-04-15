import random
def вывести(line):
    print(line)

def строка(arg):
    return str(arg)

def число(num):
    if num.isnumeric():
        return int(num)

    else:
        return f"ОШИБКА. {num} НЕВОЗМОЖНО ПЕРЕВЕСТИ В ЧИСЛО"

def округли(num):
    return round(num)

def число_ли(num):
    return num.isnumeric()

def строка_или_число(inp):
    return inp.isalnum()

def считай(*args):
    if len(args) > 0:
        return input(args[0])

    else:
        return input()

def тип(inp):
    return type(inp)

def соедини(*args):
    if len(args) == 2:
        return args[1].join(args[0])

    elif len(args) == 1:
        return ''.join(args[0])

    else:
        return "ОШИБКА"

def раздели(*args):
    if len(args) == 1:
        return args[0].split()

    elif len(args) == 2:
        return args[0].split(args[1])

    else:
        return "ОШИБКА"

def список(inp):
    return list(inp)

def дробь(inp):
    return float(inp)

def минимальное_значение(inp):
    return min(inp)

def максимальное_значение(inp):
    return max(inp)

def цикл(*args):
    c = 0

    for i in range(args[0], args[1]):
        args[2 + c](args[3 + c])
        for j in range(round((len(args) - 2) / 2) - 1):
            c += 1


def если(att1, cond, att2, *args):
    if cond == "==":
        if att1 == att2:
            for i in range(0, len(args), 2):
                args[i](args[i+1])

        else:
            return

    elif cond == "~=":
        if att1 != att2:
            for i in range(0, len(args), 2):
                args[i](args[i+1])

        else:
            return

def сложи(*args):
    if len(args) == 1 and isinstance(args[0], list):
        res = 0
        for i in args[0]:
            res += i

        return res

    elif isinstance(args[0], int):
        return sum(args)

#def круговая_циферка():
    #return 3.14159265358979323846264338327950288419716939937510

круговая_циферка = 3.14159265358979323846264338327950288419716939937510

def казнить(lst, index):
    del lst[index]
    return lst

def длина_аршин(atr):
    return len(atr)

def добавить(lst, element):
    return lst.append(element)

def расширить(lst, element):
    return lst.extend(element)

def сортировать_байкалом(lst):
    return sorted(lst)

def случайная_циферка(minimalo, maximalo):
    return random.randint(minimalo, maximalo)

def мухлёж_гадкий(value):
    random.seed(value)

def выбор_списочка(lst):
    return random.choice(lst)

def перемешать(lst):
    return random.shuffle(lst)

def большие_буковки(arg):
    return arg.upper()

def маленькие_буковки(arg):
    return arg.lower()

def выбрать_случайно(arg):
    return random.choice(arg)

def розыск(arg, arg2):
    return arg.index(arg2)