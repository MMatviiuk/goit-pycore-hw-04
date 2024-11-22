"""
Цей модуль надає функцію для розрахунку загальної та середньої заробітної плати
з файлу, який містить дані про заробітні плати. Файл повинен мати рядки у форматі: ім'я,зарплата.
"""

from typing import Tuple

def total_salary(path: str) -> Tuple[int, int]:
    """
    Розраховує загальну та середню заробітну плату з файлу.

    Файл повинен містити рядки у форматі: ім'я,зарплата.
    Ця функція читає файл, розраховує загальну та середню зарплату,
    і повертає їх як кортеж (загальна сума, середня зарплата).

    Параметри:
    path (str): Шлях до файлу з даними про зарплати.

    Повертає:
    Tuple[int, int]: Кортеж, що містить загальну суму зарплат та середню зарплату.

    Викидає винятки:
    FileNotFoundError: Якщо файл не знайдено.
    ValueError: Якщо файл порожній або містить некоректні дані.
    """
    try:
        # Використовуємо менеджер контексту для відкриття файлу
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Читаємо всі рядки файлу
            salary_total = 0  # Змінна для загальної суми зарплат
            number = 0  # Лічильник кількості розробників

            # Проходимо по кожному рядку і витягуємо дані про зарплату
            for line in lines:
                try:
                    # Розділяємо рядок за комою та отримуємо зарплату
                    salary = int(line.split(',')[1])
                    salary_total += salary
                    number += 1
                except (IndexError, ValueError):
                    raise ValueError(f"Некоректний формат даних у рядку: {line.strip()}")

    except FileNotFoundError as exc:
        raise FileNotFoundError('Файл не знайдено') from exc

    # Якщо файл порожній, викидаємо виняток
    if number == 0:
        raise ValueError('Файл із зарплатами порожній')

    # Розраховуємо середню зарплату
    average_salary = int(salary_total / number)
    return (salary_total, average_salary)

if __name__ == '__main__':
    # Виводимо результати для різних файлів

    print('Нормальний файл:')
    try:
        total, average = total_salary('salary_normal.txt')
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    print('Порожній файл:')
    try:
        total, average = total_salary('salary_empty.txt')
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    print('Файл відсутній:')
    try:
        total, average = total_salary('salary_no_file.txt')
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()
