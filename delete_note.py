# delete_note.py

from datetime import datetime

def create_note():
    """Создает новую заметку."""
    note = {}
    note["name"] = input(
     """Здравствуйте профессор, добро пожаловать в Информационный Центр базы данных НИИАЗЧАЭс. 
        Введите имя пользователя для обновления пунктов плана: """)
    note["title"] = input("Введите заголовок пункта плана: ")
    note["description"] = input("Введите описание вышеуказанного пункта плана: ")
    note["status"] = input("Введите статус вышеуказанных пунктов (новый, в процессе, выполнено): ")
    while True:
        try:
            date_str = input("Введите дату создания (ДД.ММ.ГГГГ): ")
            note["created_date"] = datetime.strptime(date_str, "%d.%m.%Y").strftime("%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ.")
    while True:
        try:
            deadline_str = input("Введите дату изменения плана (ДД.ММ.ГГГГ): ")
            note["deadline"] = datetime.strptime(deadline_str, "%d.%m.%Y").strftime("%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ.")
    return note


def display_notes(notes):
    """Отображает список заметок."""
    if not notes:
        print("Список заметок пуст.")
        return

    print("\nТекущий пунк плана: ")
    for i, note in enumerate(notes, 1):
        print(f"{i}.")
        for key, value in note.items():
            print(f"   {key.capitalize()}: {value}")
        print()


def delete_note(notes, criteria):
  """Удаляет заметки по заданному критерию (имя или заголовок)."""
  deleted_count = 0
  updated_notes = [] # Создаем новый список для хранения оставшихся заметок
  for note in notes:
    if criteria.lower() not in note['name'].lower() and criteria.lower() not in note['title'].lower() :
      updated_notes.append(note) # Если критерий не совпадает, сохраняем заметку
    else:
        deleted_count += 1


  if deleted_count > 0:
      print(f"Успешно удален следующий пункт плана {deleted_count} .")
      return updated_notes # Возвращаем обновленный список
  else:
      print("Пункт плана с таким именем пользователя или заголовком не найдено.")
      return notes # Возвращаем оригинальный список


def main():
    """Основная функция программы."""
    notes = []

    while True:
        action = input("Выберите действие (добавить, удалить, показать, выйти): ").lower()

        if action == "добавить":
            note = create_note()
            notes.append(note)
        elif action == "удалить":
             if not notes:
               print("Список пунктов плана пуст. Нечего удалять.")
               continue

             criteria = input("Введите имя пользователя или заголовок плана для удаления следуеющий пунктов: ")
             notes = delete_note(notes, criteria) # Присваиваем результат функции

        elif action == "показать":
            display_notes(notes)
        elif action == "выйти":
            break
        else:
            print("Неизвестное действие.")


if __name__ == "__main__":
    main()
