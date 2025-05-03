tasks = {}

for _ in range(3):
    date = input("Введите дату: ")

    # Проверка на команду exit
    if date.lower() == "exit":
        print("Спасибо за использование! До свидания!")
        break

    task = input("Введите задачу: ")

    # Проверка на команду exit для задачи
    if task.lower() == "exit":
        print("Спасибо за использование! До свидания!")
        break

    tasks[date] = task

# Выводим введенные задачи, если не была введена команда exit
if len(tasks) > 0:
    print("\nВведенные задачи:")
    for date, task in tasks.items():
        print(f"{date}: {task}")
