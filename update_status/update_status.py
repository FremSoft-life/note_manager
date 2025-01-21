# update_status.py

def display_current_status(current_status):
    """Отображает статус заметки."""
    print(f"Текущий статус заметки: \"{current_status}\"")

def get_new_status(valid_statuses):
    """Запрашивает у пользователя статус и проверяет его корректность."""

    while True:
    print("\n Выберите новый статус заметки:")
    for i, status in enumerate(valid_statuses):
    print(f"{i+1}. {status}")

    try:
    user_choice = int(input("Ваш выбор: "))
    if 1 <= user_choice <= len(valid_statuses):
    return valid_statuses[user_choice - 1]
    else:
    print("Некорректный ввод. Пожалуйста, выберите число из списка.")
    except ValueError:
    print("Некорректный ввод. Пожалуйста, введите число.")


def update_and_display_status(current_status, new_status):
    """Обновляет статус и выводит результат."""
    current_status = new_status
    print(f"\nСтатус заметки успешно обновлён на: \"{current_status}\"")
    return current_status


def main():
    """Основная функция."""

    current_status = "в процессе" # Начальный статус
    valid_statuses = ["выполнено", "в процессе", "отложено"]

    display_current_status(current_status)

    new_status = get_new_status(valid_statuses)
    current_status = update_and_display_status(current_status, new_status)


if __name__ == "__main__":
    main()
def get_new_status(valid_statuses):

    user_input = input("Введите новый статус (или число из списка): ").lower()
    if user_input in valid_statuses:
    return user_input

def main():
    note = {"status": "в процессе"} # Словарь для хранения информации о заметке

    note["status"] = update_and_display_status(note["status"], 'new_status')

    print(note) # Вывод словаря с обновленным статусом
