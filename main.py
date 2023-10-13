from collections import UserDict

class Field:
    def __init__(self, value:str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value            


class Phone(Field):
    def __init__(self, value:str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError
        self.value = value            


class Record:
    def __init__(self, name):
        self.name = Name(name)         
        self.phones = []

    def add_phone(self, phone_add):
        self.phones.append(Phone(phone_add))
        x = [str(lt) for lt in self.phones]
       
    def remove_phone(self, phone_remove):
        self.phones.remove(self.find_phone(phone_remove))

    def find_phone(self, phone_find):
        for x in self.phones:
            if x.value == phone_find:
                return x

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone) in self.phones:
            lst_phones = [str(lt) for lt in self.phones]
            phone_index = lst_phones.index(old_phone)
            self.phones[phone_index] = Phone(new_phone)
        else: 
            raise ValueError
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
        def add_record(self, record: Record):
            self[str(record.name)] = record

        def find(self, find_name) -> Record:
            if find_name in self.data.keys():
                return self.get(find_name)

        def delete(self, name):
            if name in self.data.keys():
                self.data.pop(name)
        
        def __str__(self):
            return f"Name: {self.data.keys()}, Phones: {str(self.data.values())}"
