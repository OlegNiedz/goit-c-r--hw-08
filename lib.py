import re
from datetime import datetime as dtdt, timedelta
from collections import UserDict, UserList


def input_error(func):  # Dekorator @input_error
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Value error.")
        except KeyError:
            print("No such name found")
        except IndexError:
            print("Not found")
        except TypeError:
            print("Not found")
        except Exception as e:
            print(f"Error: {e}")

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

    def __normalize_phone__(self, phone: str):
        ptrn = r"[\d\+]+"
        phone = "".join(re.findall(ptrn, phone))
        phone.strip()
        return phone

        #     raise ValueError("Invalid number! (must be 10 digits)")

    @input_error
    def find_phone(self, phone: str):
        phone = self.__normalize_phone__(phone)
        if self.__phone_exist__(phone):
            return self.data[self.data.index(phone)]
        else:
            raise(IndexError)

    @input_error
    def set_phone(self, phone: str):
        phone = self.__normalize_phone__(phone)
        if len(phone) != 10 or self.__phone_exist__(phone):
            print("Phone exist or Invalid format! (must be 10 digits)")
            raise(ValueError)
        else:
            self.data.append(phone)
            

    @input_error
    def edit_phone(self, phone:str, new_phone=""):
        phone = self.__normalize_phone__(phone)
        if self.__phone_exist__(phone):
            new_phone = self.__normalize_phone__(new_phone)
            if len(new_phone) != 10 or self.__phone_exist__(new_phone):
                print("Phone exist or Invalid format! (must be 10 digits)")
                raise(ValueError)
            else:
                self.data[self.data.index(phone)] = new_phone

    @input_error
    def delete_phone(self,phone):
        if self.__phone_exist__(phone):
            self.data.remove(phone)
        else:
            raise(ValueError)

    @input_error
    def get_phones(self):
        if self.data==():
            print("Phones is empty!")
        else: 
            return self.data


class Birthday(Field):
    def __init__(self, birthday=None):
        self._birthday = None

    
    @property
    def birthday(self):
        return self._birthday

    
    @birthday.setter
    def birthday(self, value):
        try:
            self._birthday = dtdt.strptime(value, "%d.%m.%Y").date()
        except:
            print("Invalid date format. Use DD.MM.YYYY")

    
    @property
    def next_birthday(self) -> dtdt.date:
        today = dtdt.today()
        year = (today.year + 1 if self._birthday.month < today.month else today.year)
        return dtdt(year=year, month=self._birthday.month, day=self._birthday.day).date()
    
    def __str__(self):
        return f"{dtdt.strftime(self.birthday,"%d.%m.%Y")}"

    def __repr__(self) -> str:
        return f"{dtdt.strftime(self.birthday,"%d.%m.%Y")}"


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

    @input_error
    def show_birthday(self,added_str=None):
        print(f"{self.name.value:15} birthday: {self.birthday}",end=added_str)

    def __str__(self):
        return f"Contact: {self.name.value:15}, phones: {'; '.join(p for p in self.phones)}"

    def __repr__(self) -> str:
        return f"Contact: {self.name.value:15}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):

    @input_error
    def set_record(self, record: Record):

        if record.name.value in self.data:
            print(f"Contact '{record.name.value}' exist!")
            raise(ValueError)
        else:
            self.data[record.name.value] = record
            print(record)
    
    @input_error
    def get_record(self, record_name: str) -> Record:
        if record_name in self.data.keys():
            return self.data.get(record_name)
        else:
            print(f"Record {record_name} don't found!")
            return None
    @input_error
    def show_all(self):
        for record_name in self.data:
            print(self.data.get(record_name))
    
    @input_error
    def delete_record(self, record_name):
        if record_name in self.data.keys():
            self.data.__delitem__(record_name)
            if record_name in self.data.keys():
                raise(ValueError)
            else:
                print(f"contact {record_name} deleted")