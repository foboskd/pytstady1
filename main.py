tasks = []

for _ in range(3):
    date = input("Введите дату: ")
    task = input("Введите задачу: ")
    tasks.append(f"{date} {task}")

for entry in tasks:
    print(entry)
