Задание 1 (greetings.py): Основные переменные Созданы базовые переменные для заметки: username, title, content, status, created_date, issue_date. 
Вывод значений организован через print.
Содержание:
name = 'Arni'
print (name)

title = 'DZ'
print (title)

content = 'переменые'
print (content)

status = 'в процессе'
print (status)

created_date = 'дата создания заметки'
print (created_date)

issue_date = 'дата истечения заметки (дедлайн)'
print (issue_date)


Задание 2 (date_changer.py): Изменение формата вывода даты Реализовано преобразование формата отображения дат для пользователя, исключив год при 
выводе переменных created_date и issue_date.
Содержание:
created_date = '19 марта 2024'
print(created_date)
temp_created_date = created_date[:-5]
print(temp_created_date)


Задание 3 (add_input.py): Ввод данных через input Переменные инициализируются через пользовательский ввод (input). Реализованы подсказки для 
пользователя о том, как вводить данные, включая формат дат.
Содержание:
from importlib.resources import contents

username=input()
#"ffadeev1998@mail.ru"
title=input()
#"заголовок заметки"
contents=input()
#"Текст заметки"
status=input()
#"Готово"
created_date=input()
#("29.12.2024")
issue_date=input()
#("29.12.2024")


Задание 4 (add_list.py): Добавление списка заголовков Пользователь вводит три заголовка, которые сохраняются в список. Введенные данные 
отображаются, включая список заголовков.
Содержание:
info = [1, 2, 3]
info2 = [1, 1.7, 'Строка', [4, 5, 'Строка 2']]

names = ['Название произведения', 'Введение',
         'Оглавление',
         ]
print(names[:])

result = names.append('Глова 1,Глова 2,Глова 3')
print(names)


Задание 5 (final.py): Использование словаря Все данные организованы в словарь для заметки, включая: Поля: username, content, status, 
created_date, issue_date. Список заголовков как значение ключа titles. Все данные выводятся на экран в структурированном виде.
Содержание:
new_list_of_employees = []
employee_data = ["ФИО", "Дата рождения", "Место рождения", "Место проживания", "Номер телефона", "Образование"]
print (employee_data)
print('\n'.join(employee_data))
list_numbering = (1, 2, 3, 4, 5, 6, 7)

print (list_numbering)

print (list_numbering[0], employee_data[0])
print (list_numbering[1], employee_data[1])
print (list_numbering[2], employee_data[2])
print (list_numbering[3], employee_data[3])
print (list_numbering[4], employee_data[4])
print (list_numbering[5], employee_data[5])
