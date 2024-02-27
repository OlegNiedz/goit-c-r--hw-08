• Серіалізація та десеріалізація даних з використанням pickle 
• Робота з файлами

Формат здачі: Розмістіть файли з розв'язанням у репозиторії goit-pycore-hw-08, та прикріпіть лінки до них у відповідь на домашнє завдання.

Поїхали!🚀


В цьому домашньому завданні ви повинні додати функціонал збереження адресної книги на диск та відновлення з диска.

Для минулого домашнього завдання ви маєте вибрати pickle протокол серіалізації/десеріалізації даних та реалізувати методи, які дозволять зберегти всі дані у файл і завантажити їх із файлу.

Головна мета, щоб застосунок не втрачав дані після виходу із застосунку та при запуску відновлював їх з файлу. Повинна зберігатися адресна книга з якою ми працювали на попередньому сеансі.


Реалізуйте функціонал для збереження стану AddressBook у файл при закритті програми і відновлення стану при її запуску.

Приклади коду які стануть в нагоді.

Серіалізація з pickle
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


Інтеграція збереження та завантаження в основний цикл

def main():
    book = load_data()

    # Основний цикл програми

    save_data(book)  # Викликати перед виходом з програми


Ці приклади допоможуть вам у реалізації домашнього завдання.


Критерії оцінювання:

Реалізовано протокол серіалізації/десеріалізації даних за допомогою pickle
Всі дані повинні зберігатися при виході з програми
При новому сеансі Адресна книга повинна бути у застосунку, яка була при попередньому запуску.

Формат здачі: Розмістіть файли з розв'язанням у репозиторії goit-pycore-hw-08, та прикріпіть лінки до них у відповідь на домашнє завдання.

Формат оцінювання: залік/не залік
