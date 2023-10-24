#Напишите фрагмент кода, который регистрирует транзакции, совершаемые пользователями
# пример ввода
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2),
                (1001, 1)]

# Создаем словарь для хранения статистики пользователей
user_statistics = {}

for user_id, transaction_type in transactions:
    if user_id not in user_statistics:
        user_statistics[user_id] = {1: 0, 2: 0, 3: 0, 'mft': 0, 'lft': 0}

    user_statistics[user_id][transaction_type] += 1

# Обновляем наиболее и наименее частую транзакции
for user_id, stats in user_statistics.items():
    stats['mft'] = max(stats, key=lambda k: (k != 'mft', stats[k]))
    stats['lft'] = min(stats, key=lambda k: (k != 'lft', stats[k]))

# Если пользователь не совершил ни одной транзакции, установим значения по умолчанию
for user_id, stats in user_statistics.items():
    for transaction_type in [1, 2, 3]:
        if transaction_type not in stats:
            stats[transaction_type] = 0

# Выводим статистику пользователей
print(user_statistics)

