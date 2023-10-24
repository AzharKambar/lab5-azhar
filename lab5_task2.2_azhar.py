#Напишите фрагмент кода, который использует словарь из задания 2.1 и
# проверяет, выполнил ли учащийся все 6 заданий — 4 задания, 2 лабораторных работы и
# 2 теста (4 балла за задания, 2 балла за лабораторные работы и 2 балла за тесты).
# Сохраните результат в новом словаре как submit_check, где вы сохраните имя студента (ключ) и
# его скорость отправки (значение) как количество отправленных действий.

try:
    # пример словаря информации о студенте
    student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}

    # проверяем выполнил ли учащийся все 6 заданий
    submission_check = {}
    submitted_activities = 0
    #задаем условие для проверки
    if 'assignment' in student and len(student['assignment']) == 4:
        submitted_activities += 4
    if 'lab' in student and len(student['lab']) == 2:
        submitted_activities += 2
    if 'test' in student and len(student['test']) == 2:
        submitted_activities += 2

    submission_check[student['name']] = submitted_activities

    # выводим на экран
    print(submission_check)

except ValueError:
    print("Ввод неверный")