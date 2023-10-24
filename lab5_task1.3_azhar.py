#Напишите фрагмент кода, который использует список из задачи 1.2
#создает три новых списка — list_vow, list_cons, list_symb.
# List_vow содержит гласные из исходного списка, list_cons содержит согласные, а list_sym содержит символы

try:
    #вводим кортеж
    vvod= [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

    #инициализируем пустые списки
    list_vow = []
    list_cons = []
    list_sym = []

    #определяем функцию, проверяющую, является ли символ гласной
    def vowel_define(char):
        return char in 'aeiou'

    #перебираем  список ввода и классифицируем символы
    for char, count in vvod:
        if vowel_define(char):
            list_vow.append((char, count))
        elif char.isalpha(): #возвращает True, если строка состоит только из алфавитных символов
            list_cons.append((char, count))
        else:
            list_sym.append((char, count))

    #выводим получившиеся строки
    print("list_vow =", list_vow)
    print("list_cons =", list_cons)
    print("list_sym =", list_sym)

except ValueError:
    print("Ввод неверный")