class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, number):
        if not self.is_valid(number):
            raise ValueError("Invalid phone number")
        super().__init__(number)

    @staticmethod
    def is_valid(number):
        return len(number) == 10 and number.isdigit()

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add_phone(self, phone):
        if Phone.is_valid(phone):
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Invalid phone number")

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
        else:
            raise KeyError("Phone number not found")

    def edit_phone(self, old_phone, new_phone):
        if not Phone.is_valid(new_phone):
            raise ValueError("Invalid new phone number")

        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
        else:
            raise KeyError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        else:
            raise KeyError("Phone number not found")

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, name, phone):
        if name in self.data:
            self.data[name].add_phone(phone)
        else:
            self.data[name] = Record(name, phone)

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("Name not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Name not found")

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."

    return wrapper

@input_error
def handle_hello():
    return "How can I help you?"

@input_error
def handle_add(command, address_book):
    _, name, phone = command.split()
    name = name.lower()
    address_book.add_record(name, phone)
    return "Contact added."

@input_error
def handle_change(command, address_book):
    _, name, phone = command.split()
    name = name.lower()
    record = address_book.find(name)
    record.edit_phone(record.phones[0].value, phone)
    return "Contact changed."

@input_error
def handle_phone(command, address_book):
    _, name = command.split()
    name = name.lower()
    record = address_book.find(name)
    return f"Phone number for {name}: {record.phones[0].value}"

@input_error
def handle_delete(command, address_book):
    _, name = command.split()
    name = name.lower()
    address_book.delete(name)
    return f"Deleted {name}"

@input_error
def handle_all(address_book):
    result = "All records:\n"
    for name, record in address_book.data.items():
        result += f"{name}: {', '.join([p.value for p in record.phones])}\n"
    return result

def main():
    address_book = AddressBook()
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print(handle_hello())
        elif command.startswith("add"):
            print(handle_add(command, address_book))
        elif command.startswith("change"):
            print(handle_change(command, address_book))
        elif command.startswith("phone"):
            print(handle_phone(command, address_book))
        elif command == "all":
            print(handle_all(address_book))
        elif command.startswith("delete"):
            print(handle_delete(command, address_book))
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
