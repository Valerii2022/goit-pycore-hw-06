from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("The phone number must consist of 10 digits")
        self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self):
        pass

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Phone number not found")


    def find_phone(self, phone):
        for record_phone in self.phones:
            if str(record_phone) == phone:
                return record_phone
        raise ValueError("Phone number not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            raise ValueError("Record not found.")
        

# test
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("2222222222")
jane_record.add_phone("7777777771")

book.add_record(jane_record)

for name, record in book.data.items():
    print(record)
    
print(len(book.data.items()))

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
book.delete("John")

print(len(book.data.items()))
