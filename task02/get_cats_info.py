"""
Цей модуль надає функціонал для читання та обробки інформації про котів з файлу.

Основна функція `get_cats_info` читає файл, який містить інформацію про котів,
і повертає список словників з інформацією про кожного кота.
"""

from typing import List, Dict, Union

def get_cats_info(path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Читає файл, який містить інформацію про котів, і повертає список словників.

    Файл повинен містити рядки у форматі: cat_id,name,age.

    Параметри:
    path (str): Шлях до файлу, який містить інформацію про котів.

    Повертає:
    List[Dict[str, Union[str, int]]]: Список словників, де кожен словник представляє
    одного кота з його ідентифікатором, ім'ям та віком.

    Викидає винятки:
    FileNotFoundError: Якщо файл не знайдено.
    ValueError: Якщо є проблема з форматом даних.
    """
    try:
        # Відкриваємо файл для читання з кодуванням utf-8
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Читаємо всі рядки з файлу
            cats = []  # Ініціалізуємо порожній список для зберігання інформації про котів

            # Проходимо по кожному рядку та витягуємо дані про кота
            for line in lines:
                cat_id, name, age = line.split(',')  # Розділяємо дані за комою
                cats.append({
                    'id': cat_id.strip(),  # Видаляємо зайві пробіли навколо ідентифікатора
                    'name': name.strip(),  # Видаляємо зайві пробіли навколо імені
                    'age': int(age.strip())  # Перетворюємо вік на ціле число
                })
    except FileNotFoundError as exc:
        raise FileNotFoundError('Файл не знайдено') from exc  # Викидаємо виняток, якщо файл не знайдено
    except ValueError as exc:
        raise ValueError('Некоректний формат даних') from exc  # Викидаємо виняток, якщо є проблема з даними

    return cats  # Повертаємо список з інформацією про котів

if __name__ == '__main__':
    # Приклад використання з нормальним файлом
    print('Нормальний файл:')
    try:
        cats_info = get_cats_info('task02/cats_normal.txt')
        print(cats_info)
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    # Приклад використання з порожнім файлом
    print('Порожній файл:')
    try:
        cats_info = get_cats_info('task02/cats_empty.txt')
        print(cats_info)
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    # Приклад використання з відсутнім файлом
    print('Файл відсутній:')
    try:
        cats_info = get_cats_info('task02/cats_no_file.txt')
        print(cats_info)
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()
