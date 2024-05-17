from collections import UserDict
from re import fullmatch

class IncorrectNameExeption(Exception):
    pass

class IncorrectPhoneExeption(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if value:
            self.value = value
        else:
            raise IncorrectNameExeption
    
    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, value):
        if fullmatch(r"^\d{10}$", value):
            self.value = value
        else:
            raise IncorrectPhoneExeption
    
    def __str__(self):
        return self.value

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def edit_phone(self, old_phone: str, new_phone: str):
        for i in range(len(self.phones)):
            if self.phones[i] == old_phone:
                self.phones[i] = new_phone
    
    def find_phone(self, phone: str):
        for element in self.phones:
            if element.value == phone:
                return phone
        return None

    def remove_phone(self, phone: str):
        for element in self.phones:
            if element.value == phone:
                self.phones.remove(element)

class AddressBook(UserDict):
    def show_all(self):
        for name, phones in book.data.items():
            for phone in phones:
                print(name + ": " + phone.value)

    def add_record(self, record: Record):
        self.data[record.name.value] = record.phones

    def delete(self, name: str):
        self.data.pop(name)
        print("Було видалено контакт:", name)
    
    def find(self, name: str) -> Record:
        finded_record = Record(name)
        for phone in self.data[name]:
            finded_record.add_phone(phone.value)
        return finded_record

############################

try:
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    book.show_all()

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
except IncorrectPhoneExeption:
    print("Некоректно введено номер телефону")
except IncorrectNameExeption:
    print("Некоректно введено ім'я користувача")