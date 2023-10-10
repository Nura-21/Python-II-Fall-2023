import re
import atexit

user_database = {}


def exit_program():
    write_db_to_file("user_database.txt")
    print("The database has been saved. Exit the program.")


def write_db_to_file(filename):
    with open(filename, 'w') as file:
        for username, password in user_database.items():
            file.write(f"{username}:{password}\n")


def read_db_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                user_database[username] = password
    except FileNotFoundError:
        pass


def show_db():
    for username, password in user_database.items():
        print(f"Username: {username}, Password: {password}")


def check_password(password):
    messages = []
    if len(password) < 8:
        messages.append("The password must contain at least 8 characters.")
    if not re.search(r'[a-z]', password):
        messages.append(
            "The password must contain at least one lowercase letter.")
    if not re.search(r'[A-Z]', password):
        messages.append(
            "The password must contain at least one uppercase letter.")
    if not re.search(r'[0-9]', password):
        messages.append("The password must contain at least one number.")
    if not re.search(r'[+-_!@#$%^&*?]', password):
        messages.append(
            "The password must contain at least one special character.")
    return messages


def add_user():
    username = input("Your login: ")
    password = input("Your password: ")

    messages = check_password(password)

    if not messages:
        user_database[username] = password
        print("User added successfully.")
    else:
        print("Password does not meet requirements:")
        for message in messages:
            print(message)


read_db_from_file("user_database.txt")

while True:
    print("1 -> Show database data")
    print("2 -> Add user")
    print("3 -> Exit")
    choice = input("Pick option: ")
    if choice == '1':
        show_db()
    elif choice == '2':
        add_user()
    elif choice == '3':
        break
    else:
        print("Pick option from list")

atexit.register(exit_program)
