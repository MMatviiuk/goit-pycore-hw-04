# README: Домашнє завдання - Робота з файлами та модульною системою

## Опис проекту

Цей проект містить виконання кількох завдань, що вчать процювати з файлами, обробляти текстову інформацію, використовувати менеджери контексту та будувати консольні застосунки для керування даними. Всі завдання розроблені для розуміння роботи з текстовими файлами, побудови рекурсивного скрипту для перегляду вмісту директорії, а також для створення консольного бота-помічника для керування контактами.

## Завдання

1. **Розрахунок заробітної плати**
   
   Завдання полягає у створенні функції `total_salary(path)`, яка аналізує текстовий файл з інформацією про місячні заробітні плати розробників. Кожен рядок файлу містить ім'я розробника та його зарплату, розділені комою. Функція повинна:
   - Відкрити файл з використанням менеджера контексту `with` для безпечного доступу до даних.
   - Обробити всі рядки, розрахувавши загальну суму зарплат та їх середнє значення.
   - Повернути кортеж з двох значень: загальної суми зарплат та середньої зарплати.
   - Обробляти можливі помилки, такі як відсутність файлу або некоректний формат даних.

2. **Інформація про котів**

   Створіть функцію `get_cats_info(path)`, яка читає файл, що містить інформацію про котів. Кожен рядок файлу має формат: `cat_id,name,age`, де `cat_id` - унікальний ідентифікатор кота, `name` - ім'я кота, `age` - вік кота. Функція повинна:
   - Відкрити файл за допомогою менеджера контексту `with`.
   - Прочитати дані та створити список словників, де кожен словник містить інформацію про кота (ключі: "id", "name", "age").
   - Повернути цей список.
   - Обробляти можливі помилки, наприклад, коли файл не знайдено або якщо дані у файлі некоректні.

3. **Виведення структури директорії**

   Розробіть скрипт, який приймає шлях до директорії як аргумент командного рядка та виводить вміст цієї директорії. Скрипт має:
   - Виводити всі файли та піддиректорії, використовуючи різні кольори для зручності сприйняття (за допомогою бібліотеки `colorama`).
   - Обробляти рекурсивно всі піддиректорії, додаючи відповідні відступи для індикації рівня вкладеності.
   - Використовувати бібліотеку `pathlib` для роботи з файловою системою.
   - Обробляти можливі помилки, такі як неправильний шлях до директорії або відсутність прав доступу.

4. **Бот-помічник**

   Напишіть консольного бота-помічника для керування контактами. Бот повинен виконувати такі функції:
   - **Додавання нового контакту**: Команда `add [ім'я] [номер]` додає новий контакт до словника контактів.
   - **Зміна існуючого контакту**: Команда `change [ім'я] [новий номер]` оновлює номер телефону для існуючого контакту.
   - **Перегляд контактів**: Команда `phone [ім'я]` повертає номер телефону для вказаного контакту, а команда `all` виводить усі збережені контакти.
   - **Привітання та завершення роботи**: Команди `hello` та `exit` відповідно вітають користувача та завершують роботу бота.
   - Використовуйте функцію `parse_input()`, щоб розібрати введення користувача на команду та її аргументи.
   - Бот має працювати у нескінченному циклі, очікуючи команди від користувача, та завершувати роботу після введення команди `exit`.

## Вимоги

- **Python 3.x**
- Бібліотеки: `datetime`, `random`, `re`, `typing`, `colorama`

## Як використовувати

1. Клонуйте репозиторій із програмою.
2. Встановіть всі необхідні залежності.
3. Запустіть відповідний файл для виконання потрібного завдання.
