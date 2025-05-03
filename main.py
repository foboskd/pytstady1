tasks = {}

for _ in range(3):
    date = input("Введите дату: ")
    task = input("Введите задачу: ")
    tasks[date] = task

exit = input("Введите команду: ")

if exit == 'exit':
    print("Спасибо за использование! До свидания!")
