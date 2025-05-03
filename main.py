today = []
tomorrow = []
other = []

while True:
    # Запрашиваем дату
    date = input("Введите дату: ")

    # Проверка на команду exit
    if date.lower() == "exit":
        print("Спасибо за использование! До свидания!")
        break

    # Проверка на команду "Сохранить задачи"
    if date.lower() == "сохранить задачи":
        # Выводим все списки с задачами
        print("\nЗадачи на сегодня:")
        for task in today:
            print(task)

        print("\nЗадачи на завтра:")
        for task in tomorrow:
            print(task)

        print("\nДругие задачи:")
        for task in other:
            print(task)

        break

    # Запрашиваем задачу
    task = input("Введите задачу: ")

    # Проверка на команду exit для задачи
    if task.lower() == "exit":
        print("Спасибо за использование! До свидания!")
        break

    # Проверка на команду "Сохранить задачи"
    if task.lower() == "сохранить задачи":
        # Выводим все списки с задачами
        print("\nЗадачи на сегодня:")
        for task in today:
            print(task)

        print("\nЗадачи на завтра:")
        for task in tomorrow:
            print(task)

        print("\nДругие задачи:")
        for task in other:
            print(task)

        break



    # Добавляем задачу в соответствующий список
    if date == "Сегодня":
        today.append(task)
    elif date == "Завтра":
        tomorrow.append(task)
    else:
        other.append(task)
