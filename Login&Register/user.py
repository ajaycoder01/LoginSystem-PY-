###: Login and Registration System Using File Handling

# . Allow a new user to register with a username and password.
# . Store the user credentials in users.txt.
# . Prevent registration if the username already exists.
# . Allow registered users to login.
# . Verify the entered username and password from the file.
# . Display an appropriate message for successful login or incorrect credentials.


FILE_NAME = "users.txt"

def register():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split("|")

                if stored_username == username:
                    print("Username already exists!")
                    return

    except FileNotFoundError:
        pass

    with open(FILE_NAME, "a") as file:
        file.write(f"{username}|{password}\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                stored_username, stored_password = line.strip().split("|")

                if stored_username == username:

                    if stored_password == password:
                        print("Login successful!")
                        return
                    else:
                        print("Incorrect password!")
                        return

        print("Username not found.")

    except FileNotFoundError:
        print("No registered users found. Please register first.")


def main():
    while True:
        print("\n========== LOGIN SYSTEM ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
