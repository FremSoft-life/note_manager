# check_deadline.py

from datetime import datetime, timedelta

def get_current_date():
    """Возвращает текущую дату в формате ДД-ММ-ГГГГ."""
    return datetime.now().strftime("%d-%m-%Y")

def get_deadline_date():
    """Приветствует пользователя, напоминает о экспериментах и запрашивает дату."""
    input("""Здравствуйте Професор Койманов, напоминаю, что скоро необходимо 
        провести ряд экспериментов на следующих объектах №1-445 и №2-543.
        Нажмите Enter, чтобы продолжить...""") # Простое приветствие, ожидает Enter

    while True:
        date_str = input("""Введите дату проведения ближайшего эксперимента в формате 
        ДД.ММ.ГГГГ (например, 26.05.1986): """)
        try:
            deadline_date = datetime.strptime(date_str, "%d.%m.%Y")
            return deadline_date
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ.")

def calculate_date_difference(deadline_date):
    """Рассчитывает разницу между датой эксперимента и текущей датой."""
    current_date = datetime.now()
    difference = deadline_date - current_date
    return difference

def display_deadline_status(difference):
    """Выводит сообщение о статусе эксперимента."""
    if difference > timedelta(0):
        days_remaining = difference.days
        if days_remaining == 0:
           print("Эксперимент сегодня!")
        elif days_remaining == 1:
            print("До эксперимента остался 1 день.")
        else:
            print(f"До эксперимента осталось {days_remaining} дней.")
    else:
        days_past = abs(difference.days)
        if days_past == 1:
            print("Внимание! Эксперимент истёк 1 день назад.")
        else:
            print(f"Внимание! Эксперимент истёк {days_past} дней назад.")

def main():
    """Основная функция программы."""
    print(f"Текущая дата: {get_current_date()}")
    deadline_date = get_deadline_date()
    difference = calculate_date_difference(deadline_date)
    display_deadline_status(difference)

if __name__ == "__main__": # Исправлено условие
    main()
