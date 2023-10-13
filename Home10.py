from main import Field, Name, Phone, AddressBook, Record

def input_error(f):
    def inner(*args):
        try:
            return f(*args)
        except IndexError:
            return "Give me name and phone please" 
        except KeyError:
            return 'User not in dict'
        except TypeError:
            return 'There is no such request'
    return inner

records = AddressBook()


@input_error
def add_record(*args):
    rec_id = args[0]
    rec_value = args[1]
    if rec_id in records.keys():
        return 'Users is empty'
    new_record = Record(rec_id) 
    new_record.add_phone(rec_value)
    records[rec_id] = new_record
    

@input_error
def change_record(*args):
    rec_id = args[0]
    old_phone = args[1]
    new_phone = args[2]
    records.find(rec_id).edit_phone(old_phone, new_phone)
    return f'Change {rec_id = }, {new_phone = }'


@input_error
def phone_record(*args):
    rec_id = args[0]
    if rec_id not in records:
        raise KeyError
    return f'Phone: {records.get(rec_id)}'


def hello_func(*args):
    return 'How can I help you?'


@input_error
def show_all_func(*args):
    for v in records.values():
        return v

def unknown(*args):
    return 'Unknown command. Try again'


COMMANDS = {add_record: 'add',
            change_record: 'change',
            phone_record: 'phone',
            hello_func: 'hello',
            show_all_func: 'show all',}


def parser(text:str):
    for func, val in COMMANDS.items():
        if text.lower().startswith(val):
            return func, text[len(val):].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input('>>>')
        if user_input.lower() == 'exit':
            print('Good bye')
            break
        func, data = parser(user_input)
        print(func(*data))


if __name__ == '__main__':
    main()