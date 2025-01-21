# add_list.py

def get_note_data():
    """Запрашивает у пользователя данные для создания заметки, включая несколько заголовков."""

    titles = []
    for i in range(3): # Запрашиваем 3 заголовка
    title = input(f"Введите заголовок {i+1}: ")
    titles.append(title)

    content = input("Введите текст заметки: Информация об объекте ")
    tags = input("Высота, длина, ширина").split(",")
    tags = [tag.strip() for tag in tags]

    while True:
    date_str = input("21.01.2025")
    try:
    date = date_str
    break
    except ValueError:
    print("Неверный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")

    status = input("Выполнено")

    return {
    "titles": titles, # Список заголовков
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
