def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    if not args:
        return "Enter user name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    while True:
        user_input = input("Enter a command: ").strip().lower()
        if user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            command, *args = user_input.split()
            if len(args) != 2:
                print("Give me name and phone please.")
            else:
                result = add_contact(args, contacts)
                print(result)
        elif user_input.startswith("change"):
            command, *args = user_input.split()
            if len(args) != 2:
                print("Give me name and phone please.")
            else:
                result = change_contact(args, contacts)
                print(result)
        elif user_input.startswith("phone"):
            command, *args = user_input.split()
            result = show_phone(args, contacts)
            print(result)
        elif user_input == "all":
            show_all(contacts)
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
