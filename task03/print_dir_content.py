"""
Цей скрипт виводить вміст директорії, показуючи папки та файли з відступами
в залежності від їх рівня вкладеності.
"""

import sys
from pathlib import Path

from colorama import init
from colorama import Fore

# Ініціалізуємо бібліотеку colorama для автоматичного скидання кольорів після кожного використання
init(autoreset=True)

def print_dir_content(directory: str, level: int = 0) -> None:
    """
    Виводить вміст директорії з відступами, що базуються на рівні вкладеності.

    Параметри:
    directory (str): Шлях до директорії, яку треба вивести.
    level (int): Поточний рівень вкладеності для відступів. За замовчуванням 0.

    Повертає:
    None
    """
    
    # Створюємо об'єкт Path для роботи з файловою системою
    path = Path(directory)

    # Перевіряємо, чи є наданий шлях дійсною директорією
    if not path.is_dir():
        print(f"The provided path {path} is not a valid directory.")
        return

    # Визначаємо відступ для поточного рівня вкладеності
    indent = ' ' * (level * 4)
    dirs = []  # Список для зберігання всіх піддиректорій
    files = []  # Список для зберігання всіх файлів

    # Проходимо по кожному елементу в директорії
    for item in path.iterdir():
        if item.is_dir():
            dirs.append(item)  # Додаємо елемент до списку директорій, якщо це директорія
        else:
            files.append(item)  # Додаємо елемент до списку файлів, якщо це файл

    # Виводимо всі піддиректорії з відповідним кольором та відступом
    for dir_item in dirs:
        print(Fore.LIGHTBLUE_EX + f"{indent}{dir_item.name}/")
        # Рекурсивно викликаємо функцію для обробки піддиректорії
        print_dir_content(dir_item, level + 1)

    # Виводимо всі файли з відповідним кольором та відступом
    for file_item in files:
        print(Fore.LIGHTGREEN_EX + f"{indent}{file_item.name}")

# Перевіряємо, чи був переданий аргумент командного рядка з шляхом до директорії
if len(sys.argv) > 1:
    path_to_file = sys.argv[1]
    print_dir_content(path_to_file)
else:
    print('Please provide path to file')
