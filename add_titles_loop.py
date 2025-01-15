notes = [
    {
        "username": "Виталя",
        "create_date": "13.01.2025"
    },
    {
        "username": "Сергей",
        "create_date": "14.01.2025"
    },
    {
        "username": "Александр",
        "create_date": "14.01.2025"
    },
    {
        "username": "Александр",
        "create_date": "14.01.2025"
    },
    {
        "username": "Александр",
        "create_date": "14.01.2025"
    }

]

def create_not(): #1usage
    notes = {
        "username": input("введите имя пользователя"),
        "create_date": input("введите дату посещения пользователем"),
        "create_date": input("введите дату посещения пользователем"),
        "username": input("введите имя пользователя")

    }

    return note

while True:
    print("возможные операции:\n"
          "0 - Выйти\n"
          "1 - Добавить заметку\n"
          "2 - Удалить заметку")
    operation = input("Введите название операции: ")
    if operation == "0":
        break
    elif operation == "1":
        notes.append(creat.note())
