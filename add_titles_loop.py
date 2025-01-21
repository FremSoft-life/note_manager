# add_titles_loop.py

def add_titles():
    """
    Функция запрашивает у пользователя заголовки заметок и
    возвращает их в виде списка.
    """
    titles = []
    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ТТХ объекта 202 ")
        if not title: # Проверка на пустой ввод
            break
        titles.append(title)
    return titles


if __name__ == "__main__":
    print("Добавление заголовков к заметке: Скорость")
    titles = add_titles()

    if titles:
        print("\nЗаголовки заметки: Кинематика")
        for title in titles:
            print(f"- {title}")
    else:
        print("\nНе было добавлено ни одного заголовка.")
