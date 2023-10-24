#Напишите фрагмент кода, который создает словарь для хранения имени учащегося,
# оценок учащегося за задания, оценок учащегося за лабораторные работы и оценок учащегося за тесты

try:
    # создаем пустой словарь для хранения информации об учащемся
    student = {}

    # получение имени учащегося
    student['name'] = input("Введите имя учащегося: ")

    # получение оценок за задания в виде списка
    score_assignment = input("Введите оценки за задания: ")
    student['assignments'] = [int(score) for score in score_assignment.split(',')]

    # получение оценок за лабораторные работы в виде списка
    score_lab= input("Введите оценки за лабораторные работы: ")
    student['labs'] = [float(score) for score in score_lab.split(',')]

    # получение оценок за тесты в виде списка
    score_test = input("Введите оценки за тесты : ")
    student['tests'] = [int(score) for score in score_test.split(',')]

    # выводим словарь  с информацией об учащемся
    print("Информация об учащемся:", student)

except ValueError:
    print("Ввод неверный")