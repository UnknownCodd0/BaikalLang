"""
ИНИЦИАЛИЗАЦИЯ
"""
import pip

#from Baikal_Lang_FP import *
from Baikal_Lang_OOP import *

# def функция(name):
#     def _f(*newargs):
#         co = 0
#         for i in range(0, len(newargs), 2):
#             if newargs[i] == "вернуть":
#                 return newargs[i + 1]
#             newargs[i](newargs[i+1])
#             co += 2
#
#
#
#
#     globals()[name] = _f
#     del _f

# def Создать_Функцию(name):
#     def _f(*newargs):
#         co = 0
#         for i in range(0, len(newargs), 2):
#             if newargs[i] == "вернуть":
#                 return newargs[i + 1]
#             newargs[i](newargs[i + 1])
#             co += 2
#
#     globals()[name] = _f
#     del _f







"""
КОД
"""

#inp = input()
file = open(r"C:\Users\Tagir\Desktop\code.txt", encoding="UTF-8")
#file = open(inp, encoding="UTF-8")

#----ЧТЕНИЕ ФАЙЛА
for i in file:
    #ПРОВЕРКА НА ПУСТОТУ СТРОКИ
    if i != '\n':
        j = i.split()

        for k in j:
            if '#' in k:
                del j[j.index(k):]

        #print("j", j)
        #print("i", i)
        if j[0] == 'Строка':
            declaration = ' '.join(j[2:])
            #print("j[1]", j[1])
            globals()[j[1]] = Строка(j[1], declaration)
            #print(declaration)
            j = []

        elif j[0] == 'Число':
            globals()[j[1]] = Число(j[1], int(j[2]))
            j = []

        elif j[0] == 'Список':
            idk = ' '.join(j[2:])
            globals()[j[1]] = Список(j[1], eval(' '.join(j[2:])))

        elif j[0] == 'ОбъявитьДругое':
            if j[2] == 'Вид':
                tto = eval(j[3])

                if type(tto) == int:
                    globals()[j[1]] = "Тип: Число"

                elif type(tto) == str:
                    globals()[j[1]] = "Тип: Строка"

        elif j[0] == 'Функция':
            def func(j):
                if j[1] == "Вывести":
                    #ЕСЛИ КОД - СТРОКА
                    if '"' in j[2]:
                        print(str(' '.join(j[2:]).strip('()""')))

                    #ЕСЛИ КОД - ЧИСЛО
                    elif j[2].strip('()').isnumeric():
                        print(j[2].strip('()'))

                    #ЕСЛИ КОД - ПЕРЕМЕННАЯ
                    elif j[2].strip('()') in globals():
                        if isinstance(globals()[j[2].strip('()')], str):
                            print(globals()[j[2].strip('()')])
                        else:
                            print(globals()[j[2].strip('()')].value)

                    #ЕСЛИ КОД - СПИСОК
                    elif '[' in j[2]:
                        temp = ' '.join(j[2:]).strip('()')
                        print(eval(temp))
                        temp = None

                elif j[1] == "Вид":
                    def type_func(j):
                        type_temp = eval(''.join(j[2:]))

                        def temp_func(arg):
                            return arg

                        if isinstance(type_temp, Число):
                            print("Тип: Число")

                        elif isinstance(type_temp, Список):
                            print("Тип: Список")

                        elif isinstance(type_temp, Строка):
                            print("Тип: Строка")

                    type_func(j)

            func(j)

        elif j[0] == 'Если':
            if eval(j[1].strip('()')):
                a = ' '.join(j[2:]).strip('[]')
                #print(a.split(', '))

                for l in a.strip(']').split(', '):
                    l = l.strip('[]')
                    l = l.strip('()')

                    newln = []

                    for tmp in l:
                        if not tmp in ['[', ']', '(', ')']:
                            newln.append(l[l.find(tmp)])

                    newln = ''.join(newln)
                    newln = newln.split()

                    if newln[0] == 'Функция':
                        func(newln)


file.close()
#print(Hello)
#print(Один)

