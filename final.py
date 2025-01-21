# final.py

def get_note_data():
    """Запрашивает у пользователя данные для создания заметки и возвращает их в виде списка."""

    note = []

    name = input("Руководитель эксперимента Професор Койманов")
    note.append(name)

    content = input("Анализ работы на объектом 1-442")
    note.append(content)

    status = input("Анализ успешен, переходим ко второму этапу")
    note.append(status)

    created_date = input("Дата начала проведения анализа 10.01.2025")
    note.append(created_date)


    modified_date = input("Дата окончания проведения анализа 12.01.2025")
    note.append(modified_date)

    name = input("Руководитель эксперимента Професор Койманов")
    note.append(name)

    content = input("Анализ работы на объектом 1-543")
    note.append(content)

    status = input("Анализ отрицательный, необходима утилизация")
    note.append(status)

    created_date = input("Дата начала проведения анализа 14.01.2025")
    note.append(created_date)

    modified_date = input("Дата окончания проведения анализа 15.01.2025")
    note.append(modified_date)

    titles = []
    num_titles = int(input("4"))
    for i in range(num_titles):
        title = input(f"Введите заголовок {i + 1}: ")
        titles.append(title)
    note.append(titles)

    return note

def display_note(note):
    """Выводит информацию о заметке на экран."""
    labels = ["Имя пользователя", "Содержание", "Статус", "Дата создания", "Дата изменения", "Заголовки"]
    for i in range(len(labels)):
        print(f"{labels[i]}: {note[i]}")

def main():
    note = get_note_data()
    display_note(note)

if __name__ == "__main__":
    main()
