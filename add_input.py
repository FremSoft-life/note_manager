# add_input.py

def get_note_data():
    """Запрашивает у пользователя данные для создания заметки."""

    title = input("Введите заголовок заметки:Информация о объекте")
    content = input("Введите текст заметки:ТТХ объекта ")
    tags = input("Высота, ширина, длина").split(",")
    tags = [tag.strip() for tag in tags] # Удаляем пробелы вокруг тегов

    while True:
    date_str = input("21.01.2025")
    try:
    date = date_str
    break
    except ValueError:
    print("Неверный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")

    status = input("Введите статус заметки: выполнено")


    return {
    "title": title,
    "content": content,
    "tags": tags,
    "date": date,
    "status": status,
    }



def main():
    note_data = get_note_data()
    print("\nСоздана заметка:")
    for key, value in note_data.items():
    print(f"{key}: {value}")

if __name__ == "__main__":
    main()
