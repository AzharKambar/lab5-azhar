#Создайте новый словарь, используя словари из задания 2.3.
#Используйте имена учащихся в качестве ключей и сохраняйте их результаты во вложенном словаре.

#пример ввода
student_one= {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
student_two= {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

#инициализируем словарь для учащихся
students = {}

#создаем функцию для добавления студента в словарь с обработкой исключений
def stud_add(student_data):
    try:
        student_name = student_data['name']
        # удаляем ключ «имя» и назначаем остальное студенту
        del student_data['name']
        students[student_name] = student_data
    except ValueError :
        print("Ввод неверный")

#добавляем студентов в словарь
stud_add(student_one)
stud_add(student_two)

#выводим полученный словарь
print(students)