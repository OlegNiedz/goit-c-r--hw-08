import re
from datetime import datetime as dtdt, timedelta
from collections import UserDict, UserList


def input_error(func):  # Dekorator @input_error
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value=str.title(value)


class Phones(UserList):

    def __phone_exist__(self, phone: str):
        return phone in self.data

    #@input_error
    def __normalize_phone__(self, phone: str):
        ptrn = r"[\d\+]+"
        phone = "".join(re.findall(ptrn, phone))
        phone.strip()
        if len(phone) == 10:
            return phone
        else:
            raise ValueError("Invalid number! (must be 10 digits)")

    @input_error
    def find_phone(self, phone: str):
        phone = self.__normalize_phone__(phone)
        if self.__phone_exist__(phone):
            return self.data[self.data.index(phone)]
        else:
            raise IndexError

    def set_phone(self, phone: str):
        phone = self.__normalize_phone__(phone)
        if not self.__phone_exist__(phone):
            self.data.append(self.__normalize_phone__(phone))
        else:
            raise ValueError("Phone exist!")

    def edit_phone(self, phone:str, new_phone=""):
        phone = self.__normalize_phone__(phone)
        if self.__phone_exist__(phone):
            new_phone = self.__normalize_phone__(new_phone)
            if new_phone and not self.__phone_exist__(new_phone):
                self.data[self.data.index(phone)] = new_phone
            else:
                self.data.remove(phone)
        else:
            raise ValueError("Phone Not exist!")

    def get_phones(self):
        return self.data


class Birthday(Field):
    def __init__(self, birthday=None):
        self._birthday = birthday

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        try:
            self._birthday = dtdt.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    @property
    def next_birthday(self) -> dtdt.date:
        today = dtdt.today()
        year = (today.year + 1 if self._birthday.month < today.month else today.year)
        return dtdt(year=year, month=self._birthday.month, day=self._birthday.day).date()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = Phones()
        self.birthday = Birthday(None)

    @input_error
    def edit_name(self, new_name: str):
        if new_name:
            self.name = Name(new_name)
        else:
            raise ValueError

    def show_birthday(self):
        print(f"{self.name:25} birthday: {self.birthday:15}")

    def __str__(self):
        return f"Contact name: {self.name.value:25}, phones: {'; '.join(p for p in self.phones)}"

    def __repr__(self) -> str:
        return f"Contact name: {self.name.value:25}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    @input_error
    def set_record(self, record: Record):

        if record.name.value in self.data:
            raise (ValueError(f"Contact '{record.name.value}' exist!")
        else:
            self.data[record.name.value] = record

    def get_record(self, record_name: str) -> Record:
        if record_name in self.data:
            return self.data.get(record_name)
        else:
            print(f"Record {record_name} don't found!")
            return None

    def show_all(self):
        print(self)
        for record_name in self.data:
            print(self.data.get(record_name))

    def delete_record(self, record_name):
        if record_name in self.data:
            self.data.__delitem__(record_name)
