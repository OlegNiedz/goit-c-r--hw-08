from lib import AddressBook, Field, Name, Phones, Record, Birthday, dtdt, timedelta


def main():
    comands = {
        "hello": "hello (cmd)",
        "add": "create a new contact",
        "change": "change the contact",
        "show": "show contacts phone ",
        "all": "show all contacts",
        "add-ph": "add phone to contact",
        "edit-ph": "change the contacts phone",
        "add-bd": 'format "DD.MM.YYYY"',
        "show-bd": "show contacts birthday",
        "bdays": "show birthday persons (in this week)",
        "close": "close aplication",
        "exit": "exit",
    }

    def promt(
        msg_promt: str,
        variants: tuple = (),
        msg_err="",
        ignore_caps=False
        ):
        while True:
            answer = input(msg_promt)
            if ignore_caps:
                answer = answer.lower()
            if answer and not variants or answer in variants:
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
                contact_name = promt("Enter contacts Name: ",ignore_caps=True)
                if contact_name:
                    book.set_record(Record(contact_name))

            case "change":
                contact_name = promt(
                    "Enter Name: ",
                    tuple(book.data.keys()),
                    "Name incorrect!",
                    ignore_caps=True,
                )
                contact = book.get_record(contact_name)
                new_contact_name = promt("Enter new Name: ")
                if not (new_contact_name in book.data.keys()):
                    contact.edit_name(new_contact_name)

            case "add-ph": 
                if book.data:                    
                    contact_name = promt("Enter Name: ", tuple(book.data.keys()), "Name incorrect!",ignore_caps=True)
                    new_phone = promt("Enter new phone: ")
                    book.get_record(contact_name).phones.set_phone(new_phone)

            case "edit-ph":
                if book.data:
                    contact_name = promt(
                        "Enter Name: ",
                        tuple(book.data.keys()),
                        "Name incorrect!",
                        ignore_caps=True,
                    )
                    contact = book.get_record(contact_name)
                    if contact.phones:
                        old_phone = promt(
                            "Enter existing phone: ",
                            contact.phones,
                            "Phone Not found!"
                        )

                        new_phone = promt("Enter new phone: ")
                        contact.phones.edit_phone(old_phone, new_phone)
                else:
                    print(f"Adres book is empty!")

            case "show":
                contact_name = promt(
                    "Enter Name: ", tuple(book.data.keys()), "Name incorrect!",ignore_caps=True
                )
                print(book.get_record(contact_name))

            case "all":
                book.show_all()

            case "add-bd":
                contact_name = promt(
                    "Enter Name: ",
                    tuple(book.data.keys()),
                    "Name incorrect!",
                    ignore_caps=True,
                )
                contact = book.get_record(contact_name)
                contact.birthday.birthday = promt("Enter birthday DD.MM.YYYY: ")
                contact.show_birthday()

            case "show-bd":
                contact_name = promt(
                    "Enter Name: ",
                    tuple(book.data.keys()),
                    "Name incorrect!",
                    ignore_caps=True,
                )
                book.get_record(contact_name).show_birthday()

            case "birthdays":

                for record in book.data.keys():
                    record = book.get_record(record)
                    congrat_date = record.birthday.next_birthday
                    if 0 <= (congrat_date - dtdt.today().date()).days < 7:
                        match congrat_date.weekday():
                            case 5:
                                congrat_date = congrat_date.__add__(timedelta(days=2))
                            case 6:
                                congrat_date = congrat_date.__add__(timedelta(days=1))
                        added_str = f"  Congratulation: {dtdt.strftime(congrat_date,'%d.%m.%Y')} \n"
                        contact.show_birthday(added_str)

            case "close" | "exit":

                print("\nGood bye!\n")
                break

            case _:
                print("Invalid command!\n")


if __name__ == "__main__":
    main()
