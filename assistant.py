def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found. Please provide a valid name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please provide the correct number of arguments."
        except Exception:
            return "An unexpected error occurred. Please try again."
    return wrapper

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact {name} already exists"
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} changed."
    else:
        return f"Contact {name} not found"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"The phone number for '{name}' is {contacts[name]}."

@input_error
def show_all(contacts):
    if len(contacts) == 0:
        return "You have no contacts yet."   
    else:
        return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()