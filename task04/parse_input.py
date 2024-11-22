"""
Модуль, що надає функції для парсингу введення користувача.

Функції:
- parse_input(user_input: str) -> tuple: Розбирає введення користувача на команду та її аргументи.
"""

def parse_input(user_input: str) -> tuple:
    """
    Розбирає введення користувача на команду та її аргументи.

    Параметри:
    user_input (str): Рядок, введений користувачем, який містить команду та опціональні аргументи.

    Повертає:
    tuple: Кортеж, що містить команду (str) та її аргументи (список рядків).

    Приклад:
    >>> parse_input("add Mary 1234567")
    ('add', ['Mary', '1234567'])
    """
    # Розділяємо введення користувача на команду та аргументи
    cmd, *args = user_input.split()
    # Перетворюємо команду на нижній регістр для зручності обробки
    cmd = cmd.strip().lower()
    return cmd, args  # Повертаємо команду та список аргументів

if __name__ == "__main__":
    # Тестові приклади для демонстрації роботи функції parse_input
    print(parse_input('hello'))  # ('hello', [])
    print(parse_input('add Mary 1234567'))  # ('add', ['Mary', '1234567'])
    print(parse_input('change Mary 7654321'))  # ('change', ['Mary', '7654321'])
    print(parse_input('phone Mary'))  # ('phone', ['Mary'])
    print(parse_input('all'))  # ('all', [])
    print(parse_input('exit'))  # ('exit', [])
    print(parse_input('invalid_command'))  # ('invalid_command', [])
