users = {
    "john": "pass123",
    "alice": "welcome",
    "admin": "admin@123"
}

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not username or not password:
            raise ValueError("Empty input provided.")

        if username not in users:
            raise KeyError("User doesn't exist.")

        if users[username] != password:
            raise PermissionError("Incorrect password.")

        print("Login successful. Welcome", username)
        break

    except ValueError as ve:
        print("ValueError:", ve)

    except KeyError as ke:
        print("KeyError:", ke)

    except PermissionError as pe:
        print("PermissionError:", pe)

    except Exception as e:
        print("An unexpected error occurred:", e)

    attempts += 1
    print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Too many failed attempts. Account locked.")
