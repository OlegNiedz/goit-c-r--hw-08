from lib import AddressBook, Field, Name, Phones, Record, Birthday, dtdt, timedelta


def main():
    comands = {
        "hello": "hello (cmd)",
        "add": "create a new contact",
        "change": "change the contact",
        "phone": "change the contacts phone",
        "show": "show contacts phone ",
        "all": "show all contacts",
        "add-birthday": 'format "DD.MM.YYYY"',
        "show-birthday": "show contacts birthday",
        "birthdays": "show birthday persons (in this week)",
        "close": "close aplication",
        "exit": "exit",
    }

    def promt(
        msg_promt: str,
        variants: tuple = (),
        msg_err="",
        ignore_caps=False,
        allow_empty=False,
    ):
        while True:
            answer = input(msg_promt)
            if ignore_caps:
                answer = answer.lower()
            if (answer and (not variants or answer in variants)) or (
                allow_empty and not answer
            ):
                break
            else:
                print(msg_err)
        return answer

    book = AddressBook()

    print("\nWelcome to the assistant bot!\n\n        COMMANDS:")

    for command in comands:
        print(f"{command:20} - {comands[command]}")

    while True:
        command = promt(
            "Enter command:", tuple(comands.keys()), "Unknown command!", True
        )
        match command:
            case "hello":
                print("\nHow can I help you?\n")

            case "add":
                contact_name = promt(msg_promt="Enter contacts Name: ")
                if contact_name:
                    book.set_record(Record(contact_name))

            case "change":
                contact_name = promt(
                    "Enter Name: ", tuple(book.data.keys()), "Name incorrect!"
                )
                contact = book.get_record(contact_name)
                new_contact_name = promt("Enter new Name: ")
                if not (new_contact_name in book.data):
                    contact.edit_name(new_contact_name)

            case "phone":
                contact_name = promt(
                    "Enter Name: ", tuple(book.data.keys()), "Name incorrect!"
                )
                contact = book.get_record(contact_name)
                old_phone = promt(
                    "Enter existing phone (ENTER for Add New): ",
                    contact.phones,
                    "Phone Not found!",
                    allow_empty=True,
                )
                new_phone = promt(
                    f"Enter new phone (ENTER for Delete {old_phone}): ",
                    allow_empty=True,
                )
                if old_phone:
                    contact.phones.edit_phone(old_phone, new_phone)
                else:
                    contact.phones.set_phone(new_phone)

            case "show":
                contact_name = promt(
                    "Enter Name: ", tuple(book.data.keys()), "Name incorrect!"
                )
                print(book.get_record(contact_name))

            case "all":
                book.show_all()

            case "add-birthday":
                contact_name = promt(
                    "Enter Name: ", tuple(book.data.keys()), "Name incorrect!"
                )
                contact = book.get_record(contact_name)
                contact.birthday = Birthday(promt("Enter birthday DD.MM.YYYY: "))

            case "show-birthday":
                contact_name = promt(
                    "Enter Name: ", tuple(book.data.keys()), "Name incorrect!"
                )
                contact = book.get_record(contact_name).show_birthday()

            case "birthdays":

                for record in book.data:
                    record = book.get_record("")
                    congrat_date = record.birthday.next_birthday
                    if 0 <= (congrat_date - dtdt.today().date()).days < 7:
                        match congrat_date.weekday():
                            case 5:
                                congrat_date = congrat_date.__add__(timedelta(days=2))
                            case 6:
                                congrat_date = congrat_date.__add__(timedelta(days=1))

            case "close" | "exit":

                print("\nGood bye!\n")
                break

            case _:
                print("Invalid command!\n")


if __name__ == "__main__":
    main()
