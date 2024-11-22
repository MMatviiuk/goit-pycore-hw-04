"""
Цей модуль надає функції для керування словником контактів, де кожен контакт
представлений ім'ям та номером телефону.

Функції:
- add_contact(args: list[str], contacts: Dict[str, str]) -> str:
    Додає новий контакт з вказаним ім'ям та номером телефону до словника контактів.

- change_contact(args: list[str], contacts: Dict[str, str]) -> str:
    Оновлює номер телефону існуючого контакту у словнику контактів.

- show_phone(args: list[str], contacts: Dict[str, str]) -> str:
    Повертає номер телефону контакту зі словника контактів.

- show_all(contacts: Dict[str, str]) -> Union[str, Dict[str, str]]:
    Повертає всі контакти, що зберігаються у словнику контактів.

Використання:
Цей модуль може бути імпортований та використаний в інших Python скриптах для керування
контактами. Кожна функція відповідає за конкретну операцію, пов'язану з додаванням,
оновленням та отриманням інформації про контакти.
"""
from typing import Dict, Union

def add_contact(args: list[str], contacts: Dict[str, str]) -> str:
    """
    Додає новий контакт з вказаним ім'ям та номером телефону до словника контактів.

    Параметри:
    args (list[str]): Список аргументів, що містить ім'я та номер телефону.
    contacts (Dict[str, str]): Словник, що містить контакти, де ключі - це імена, а значення - номери телефонів.

    Повертає:
    str: Повідомлення про успіх або помилку, що вказує, чи був контакт успішно доданий,
    або якщо він вже існує.
    """
    if len(args) < 2:
        return "Invalid arguments. Expected name and phone."

    name, phone = args

    if name in contacts:
        return f"Contact {name} is already in contacts."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args: list[str], contacts: Dict[str, str]) -> str:
    """
    Оновлює номер телефону існуючого контакту у словнику контактів.

    Параметри:
    args (list[str]): Список аргументів, що містить ім'я та новий номер телефону.
    contacts (Dict[str, str]): Словник, що містить контакти, де ключі - це імена, а значення - номери телефонів.

    Повертає:
    str: Повідомлення про успіх або помилку, що вказує, чи був контакт успішно оновлений,
    чи якщо його не знайдено або номер не змінився.
    """
    if len(args) < 2:
        return "Invalid arguments. Expected name and phone."

    name, phone = args

    if name in contacts:
        if contacts[name] == phone:
            return f"Contact {name} already has this phone number."
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."

def show_phone(args: list[str], contacts: Dict[str, str]) -> str:
    """
    Повертає номер телефону контакту зі словника контактів.

    Параметри:
    args (list[str]): Список аргументів, що містить ім'я контакту.
    contacts (Dict[str, str]): Словник, що містить контакти, де ключі - це імена, а значення - номери телефонів.

    Повертає:
    str: Номер телефону контакту, якщо він знайдений, або повідомлення про те, що контакт не знайдено.
    """
    if len(args) != 1:
        return "Invalid arguments. Expected name."

    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts: Dict[str, str]) -> Union[str, Dict[str, str]]:
    """
    Повертає всі контакти, що зберігаються у словнику контактів.

    Параметри:
    contacts (Dict[str, str]): Словник, що містить контакти, де ключі - це імена, а значення - номери телефонів.

    Повертає:
    Union[str, Dict[str, str]]: Рядок, що вказує на відсутність контактів, якщо словник порожній,
    або повертає словник контактів.
    """
    return contacts or "No contacts."

if __name__ == "__main__":
    print()

    contacts_list = {}
    # Тестуємо add_contact
    print('Test add_contact >>>')
    # Має успішно додати контакт
    print(add_contact(["John", "123456789"], contacts_list))
    # Має вказати, що контакт вже існує
    print(add_contact(["John", "987654321"], contacts_list))
    # Має вказати на некоректні аргументи
    print(add_contact(["John"], contacts_list))
    print()

    # Тестуємо change_contact
    print('Test change_contact >>>')
    # Має успішно оновити контакт
    print(change_contact(["John", "987654321"], contacts_list))
    # Має вказати, що номер не змінився
    print(change_contact(["John", "987654321"], contacts_list))
    # Має вказати, що контакт не знайдено
    print(change_contact(["Mary", "456789123"], contacts_list))
    # Має вказати на некоректні аргументи
    print(change_contact(["John"], contacts_list))
    print()

    # Тестуємо show_phone
    print('Test show_phone >>>')
    # Має показати номер телефону для John
    print(show_phone(["John"], contacts_list))
    # Має вказати, що контакт не знайдено
    print(show_phone(["Mary"], contacts_list))
    # Має вказати на некоректні аргументи
    print(show_phone(["John", "Mary"], contacts_list))
    print()

    # Тестуємо show_all
    # Має показати всі контакти
    print(show_all(contacts_list))
    print()
