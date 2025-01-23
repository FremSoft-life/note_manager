# multiple_notes.py

from datetime import datetime

def create_note():
    """Создает новую заметку, запрашивая данные у пользователя."""

    note = {}

    note["name"] = input("Введите имя пользователя: ")
    note["title"] = input(
""" """)
    note["description"] = input("Желаете еще, чтото добавить в заметку" )
    note["status"] = input("Введите статус заметки: ")
    while True: # Цикл для проверки формата даты создания
        try:
            date_str = input("Введите дату создания (ДД.ММ.ГГГГ): ")
            note["created_date"] = datetime.strptime(date_str, "%d.%m.%Y").strftime("%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ.")

    while True: # Цикл для проверки формата дедлайна
        try:
            deadline_str = input("Введите дедлайн (ДД.ММ.ГГГГ): ")
            note["deadline"] = datetime.strptime(deadline_str, "%d.%m.%Y").strftime("%d.%m.%Y")
            break

        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ.")
    return note



def display_notes(notes):
    """Отображает список заметок."""
    print("\nСписок заметок:")
    for i, note in enumerate(notes, 1):
        print(f"{i}.")
        for key, value in note.items():
            print(f"   {key.capitalize()}: {value}")
        print()


def main():
    """Основная функция программы."""

    notes = []

    print(" Здравствуйте профессор Кайманов. Добро пожаловать в \"Архив проекта 16\"! Вы можете добавить новую заметку.")

    while True:
        note = create_note()
        notes.append(note)

        another_note = input("Хотите добавить ещё одну заметку? (да/нет): ").lower()
        if another_note != "да":
            break

    display_notes(notes)



if __name__ == "__main__":
    main()

