"""
Цей модуль містить основну функцію для запуску бота-асистента для керування контактами.

Бот взаємодіє з користувачем через командний рядок для додавання, оновлення, перегляду контактів та інші дії.

Функції:
- main(): Основна функція для запуску бота-асистента.
"""
import handlers
from parse_input import parse_input

def main():
    """
    Запускає бота-асистента для керування контактами.

    Функція безперервно запитує команди від користувача та обробляє їх відповідно:
    - 'close' або 'exit' для завершення роботи програми
    - 'hello' для привітання користувача
    - 'add' для додавання нового контакту
    - 'change' для оновлення контакту
    - 'phone' для перегляду номера телефону контакту
    - 'all' для перегляду всіх контактів

    Використовує обробники зі модуля 'handlers' для керування контактами.

    Повертає:
    None
    """
    contacts = {}  # Ініціалізуємо порожній словник для зберігання контактів

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")  # Отримуємо команду від користувача

        if not user_input:
            continue  # Пропускаємо порожні команди

        command, *args = parse_input(user_input)  # Розбираємо команду на основну частину та аргументи

        if command in ["close", "exit"]:
            print("Good bye!")
            break  # Завершуємо роботу, якщо команда "close" або "exit"

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(handlers.add_contact(args, contacts))

        elif command == "change":
            print(handlers.change_contact(args, contacts))

        elif command == "phone":
            print(handlers.show_phone(args, contacts))

        elif command == "all":
            result = handlers.show_all(contacts)
            if isinstance(result, dict):
                for name, phone in result.items():
                    print(f"{name}: {phone}")
            else:
                print(result)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
