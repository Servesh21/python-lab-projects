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
import os

def get_password():
    """
    Retrieves the password from an environment variable or prompts the user if not found.
    """
    password = os.environ.get("PASSWORD")  # Retrieve password from environment variable
    if not password:
        password = input("Enter password: ").strip()  # Prompt user if not in environment
    return password

password = get_password()

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
import logging

def redact_sensitive_info(message):
    """
    Redacts potentially sensitive information from a log message.
    This is a placeholder; implement more sophisticated redaction as needed.
    """
    redacted_message = message.replace("password", "******").replace("token", "******").replace("API key", "******")  # Example redaction
    return redacted_message

try:
    my_dict = {}
    # Simulate a KeyError
    value = my_dict["nonexistent_key"]
except KeyError as ke:
    # Log the error message, redacting any potential sensitive information.
    logging.error(redact_sensitive_info(f"KeyError: {ke}"))

    except PermissionError as pe:
        print("PermissionError:", pe)

    except Exception as e:
        print("An unexpected error occurred:", e)

    attempts += 1
    print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Too many failed attempts. Account locked.")
