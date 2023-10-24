#Напишите фрагмент кода, который использует словари из задачи 2.1 и задачи 2.2 и рассчитывает итоговую оценку учащегося по формуле:
#0,3 * 𝑎𝑣𝑒𝑟𝑎𝑔𝑒(𝑎𝑠𝑠𝑖𝑔𝑛𝑚𝑒𝑛𝑡) + 0, 5 * 𝑎𝑣𝑒𝑟𝑎𝑔𝑒(𝑙𝑎 𝑏) + 0. 2 * 𝑎𝑣𝑒𝑟𝑎𝑔𝑒(𝑡𝑒𝑠𝑡)
#Итоговая оценка может быть рассчитана только для учащихся, выполнивших не менее 4 заданий,
# в противном случае итоговая оценка равна 0. Добавьте итоговую оценку в словарь учащихся.

def calc_final_grade(student, submission_rate):
    try:
        # проверяем, существует ли учащийся и отправил ли он хотя бы 4 действия
        if student['name'] in submission_rate and submission_rate[student['name']] >= 4:
            assignment_average = sum(student['assignment']) / len(student['assignment'])
            test_average = sum(student['test']) / len(student['test'])
            lab_average = sum(student['lab']) / len(student['lab'])
            final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
            student['final_grade'] = final_grade
        else:
            student['final_grade'] = 0.0
    except ValueError :
        print("ввод неверный")

    #пример ввода
    student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
    submission_rate = {'Adam': 6}

    # рассчитаем и поставим итоговую оценку
    calc_final_grade(student, submission_rate)

    # выводим обновленный словарь
    print(student)