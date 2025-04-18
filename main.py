"""
ИНИЦИАЛИЗАЦИЯ
"""

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
#file = open(r"C:\Users\Tagir\Desktop\baikal.bkln", encoding="UTF-8")
#file = open(inp, encoding="UTF-8")
check_elif_else = False #Переменная, необходимая для обработки elif/else
if_should_continue = False #Переменная, помогающая указать значение check_elif_else
since_last_if = 0 #Переменная, считающая строки с последнего if
iselif = False #Переменная, проверяющая, находится ли

def Check_Stroka(argstr):
    if '.длина()' in argstr:
        return len(argstr[0:argstr.find('.длина()')])

    if '.загбуквы()' in argstr:
        return argstr[0:argstr.find('.загбуквы()')].upper()

    if '.малбуквы()' in argstr:
        return argstr[0:argstr.find('.загбуквы()')].lower()

def Check_Chislo(argnum) -> int:
    if '.модуль()' in argnum:
        return abs(int(argnum[0:argnum.find('.модуль()')]))

    if '.двоичное()' in argnum:
        bin(int(argnum[0:argnum.find('.двоичное()')]))

def Check_Spisok(arglist) -> list:
    if '.сортировать()' in arglist and arglist.find('.сортировать()') > arglist.find(']'):
        return sorted(eval(arglist[0:arglist.find('.сортировать()')]))

    if '.добавить(' in arglist and arglist.find('.добавить(') > arglist.find(']'):
        temp1 = eval(arglist[0:arglist.find('.добавить(')])
        temp1.append(eval(arglist[(arglist.find('.добавить(') + 10):-1]))
        return temp1



#----ЧТЕНИЕ ФАЙЛА
for i in file:
    #ПРОВЕРКА НА ПУСТОТУ СТРОКИ
    if i != '\n':
        #Деление строки файла на токены по пробелам
        j = i.split()

        #Проверка на if/elif/else
        if check_elif_else and not iselif:
            since_last_if += 1

        #Проверка на if/elif/else
        if j[0] != "Если" and j[0] != "Или" and j[0] != "Иначе":
            if since_last_if == 1:
                check_elif_else = False
                if_should_continue = False
                since_last_if = 0
                raise Exception("Неправильный синтаксис. Вы ввели другой код между блоками Если-Или-Иначе")

        #Удаление Комментариев из кода
        for k in j:
            if '#' in k:
                del j[j.index(k):]

        #Объявление переменной типа Строка
        if j[0] == 'Строка':
            declaration = ' '.join(j[2:])

            temp = Check_Stroka(declaration)

            if temp != None:
                globals()[j[1]] = Строка(j[1], temp)

            else:
                globals()[j[1]] = Строка(j[1], eval(declaration))
            j = []

        #Объявление переменной типа Число
        elif j[0] == 'Число':

            temp = Check_Stroka(j[2])

            if temp != None:
                globals()[j[1]] = temp

            else:
                globals()[j[1]] = Число(j[1], eval((j[2])))
            j = []

        #Объявление переменной типа Список
        elif j[0] == 'Список':
            idk = ' '.join(j[2:])

            temp = Check_Spisok(idk)

            if temp != None:
                globals()[j[1]] = temp

            else:
                globals()[j[1]] = Список(j[1], eval(' '.join(j[2:])))

        #Объявление переменной, имеющий значения результата Функции
        elif j[0] == 'ОбъявитьДругое':
            if j[2] == 'Вид':
                tto = eval(j[3])

                if type(tto) == int:
                    globals()[j[1]] = "Тип: Число"

                elif type(tto) == str:
                    globals()[j[1]] = "Тип: Строка"

        # Перезапись переменной, возможность совершить с ней действия типа <a = a + 1>
        elif j[0] == 'Переменная':
            globals()[j[1]] = eval(j[2])

        #Выполнение функции
        elif j[0] == 'Функция':
            #Функция func. Необходима для избежания лишних if-else в функциях Если, ДляКаждого, Пока
            def func(j):
                if j[1] == "Вывести":
                    #ЕСЛИ КОД - СТРОКА
                    if '"' in j[2]:

                        #Защита от удаления всех скобок, даже тех, которые отвечают за методы
                        if j[-1][-1][-1] == ')':
                            j[-1] = j[-1][:-1]


                        temp = Check_Stroka(Строка('t', ' '.join(j[2:]).replace('"', "").lstrip('()')).value)

                        if temp != None:
                            print(temp)

                        else:
                            print(str(' '.join(j[2:]).strip('()""').replace(';Конец', '').replace('"', '')))

                    #ЕСЛИ КОД - ЧИСЛО
                    elif j[2].strip('()').isnumeric():
                        print(j[2].strip('()'))

                    #ЕСЛИ КОД - ПЕРЕМЕННАЯ
                    elif j[2].strip('()') in globals():
                        if isinstance(globals()[j[2].strip('()')], str):
                            print(globals()[j[2].strip('()')])
                        else:
                            if isinstance(globals()[j[2].strip('()')], int):
                                print(globals()[j[2].strip('()')])
                            elif isinstance(globals()[j[2].strip('()')], Список):
                                print(globals()[j[2].strip('()')].value)
                            elif isinstance(globals()[j[2].strip('()')], list):
                                print(globals()[j[2].strip('()')])

                    #ЕСЛИ КОД - СПИСОК
                    elif '[' in j[2]:
                        temp = ' '.join(j[2:]).strip('()')
                        print(eval(temp))
                        temp = None


                #Функция вид (type, но не метакласс)
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

                #Цикл Пока (while)
                elif j[1] == 'Пока':
                    myvar = ' '.join(j[3:]).strip('[]')
                    while eval(j[2].strip('()')):
                            newln1 = []

                            for tmp1 in myvar:
                                if not tmp1 in ['[', ']', '(', ')']:
                                    newln1.append(myvar[myvar.find(tmp1)])


                            newln1 = ''.join(newln1)
                            newln1 = newln1.split(', ')

                            #print(newln1)

                            for kj in newln1:
                                kj = kj.split()
                                if 'Функция' in kj:
                                    #print('newln1', newln1)
                                    func(kj)

                                elif 'Строка' in kj:
                                    pass

                                elif 'Переменная' in kj:
                                    globals()[kj[1]] = eval(kj[2])

                #Цикл ДляКаждого (for с синтаксисом Lua + Baikal)
                elif j[1] == 'ДляКаждого':
                    print("j2", j[2][0])
                    for nest in range(int(j[2][2:]), int(j[3])):
                        globals()[j[2][0]] = i
                        a = ' '.join(j[4:]).strip('[]')
                        # print(a.split(', '))

                        #Основное тело, прогоняющее заданные в кв. скобках действия
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


            func(j)

        #Оператор Если
        elif j[0] == 'Если':
            if eval(j[1].strip('()')):
                if_should_continue = False
                a = ' '.join(j[2:]).strip('[]')

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

            else:
                if_should_continue = True

            if if_should_continue:
                check_elif_else = True

            else:
                check_elif_else = False
                since_last_if = 0

            if ';Конец' in j:
                if_should_continue = False
                check_elif_else = False
                since_last_if = 0


        #Оператор ИЛИ (elif)
        elif j[0] == 'Или':
            if check_elif_else:
                if eval(j[1].strip('()')):
                    check_elif_else = False
                    if_should_continue = False
                    iselif = False
                    since_last_if = 0



                    a = ' '.join(j[2:]).strip('[]')


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

                else:
                    if ';Конец' in j:
                        if_should_continue = False
                        check_elif_else = False
                        iselif = False
                        since_last_if = 0

                    else:
                        if_should_continue = True
                        check_elif_else = True
                        iselif = True
            else:
                raise Exception("Блок Или без Если")

        #Оператор ИНАЧЕ (else)
        elif j[0] == "Иначе":
            if check_elif_else:
                check_elif_else = False
                if_should_continue = False
                iselif = False
                since_last_if = 0
                a = ' '.join(j[1:]).strip('[]')

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

            else:
                raise Exception("Блок Иначе без Если")


        #Вывод генерация ошибки если неправильно введена команда
        else:
            raise Exception("Неправильно введенная команда")




# Закрытие файла (для оптимизации)
file.close()
