import tkinter as tk
from tkinter import ttk, messagebox
import bcrypt
import sqlite3



conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("create table if not exists users ( id integer primary key autoincrement, username text unique not null, email text unique not null, password text not null)")
conn.commit()

import bcrypt

class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes the provided password using bcrypt.

        Args:
            password: The password to hash.

        Returns:
            The bcrypt hash of the password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
import bcrypt

class PasswordManager:
    @staticmethod
    def hash_password(password):
        """Hashes the given password using bcrypt."""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    @staticmethod
    def check_password(hashed_password, user_password):
        """Checks if the given password matches the hashed password using bcrypt."""
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)
    
import sqlite3
from tkinter import messagebox

def register(user_name, email_id, pass_word, hash_password, cur, conn):
    """Registers a new user with username, email, and password."""
    username = user_name.get()
    email = email_id.get()
    password = pass_word.get()
    
    if not username or not email or not password:
        messagebox_show_error("All fields are compulsory")
        return
    
    if "@" not in email or "." not in email:
        messagebox_show_error("Enter a valid email")
        return
        
    if len(password)<6:
        messagebox_show_error("Password must be atleast 6 characters")
        return
    
    hashed_pass = hash_password(password)
    
    try:
        cur.execute("insert into users (username,email,password) values (?,?,?)",(username,email,hashed_pass))
        conn.commit()
        messagebox_show_info("Success","Registration Successful! You can log in now")
    except sqlite3.IntegrityError:
        messagebox_show_error("Username or Email already exists")

def messagebox_show_error(message):
    """Displays an error message using messagebox."""
    messagebox.showerror("Error", message)

def messagebox_show_info(title, message):
    """Displays an info message using messagebox."""
    messagebox.showinfo(title, message)
        
from tkinter import messagebox

def check_credentials(username, password, cur):
    """
    Verifies user credentials against the database.
    """
    if not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return False

    cur.execute("select password from users where username = ?", (username,))
    user = cur.fetchone()

    if user and check_password(user[0], password):
        messagebox.showinfo("Success", "Login Successful! Welcome " + username)
        return True
    else:
        messagebox.showerror("Error", "Invalid Username or Password!")
        return False

def login():
    """
    Handles user login, now using the check_credentials function.
    """
    username = user_name.get()
    password = pass_word.get()

    check_credentials(username, password, cur)
    

root = tk.Tk()
root.title("Login Form")
root.geometry("400x500")
root.resizable(False,False)

tk.Label(root,text="Username:").pack(anchor="w",padx=10,pady=2)
user_name=tk.Entry(root)
user_name.pack(fill="x",padx=10)

tk.Label(root,text="Email:").pack(anchor="w",padx=10,pady=2)
email_id=tk.Entry(root)
email_id.pack(fill="x",padx=10)

import tkinter as tk
import os

# Use environment variables or a secure configuration for sensitive data
PASSWORD = os.environ.get("PASSWORD")

root = tk.Tk()
root.geometry("400x400")

def check():
    Pas = password.get()
    # Removed hardcoded password and using the environment variable
    if Pas == PASSWORD:
        tl = tk.Toplevel(root)
        tl.geometry("150x100")
        tk.Label(tl, text="Login Success").pack()
    else:
        tl = tk.Toplevel(root)
        tl.geometry("150x100")
        tk.Label(tl, text="Login Failed").pack()

tk.Label(root,text="Username:").pack(anchor="w",padx=10,pady=2)
username = tk.Entry(root)
username.pack(anchor="w",padx=10,pady=2)

import tkinter as tk
import os

# Use environment variables for sensitive information
PASSWORD = os.environ.get("PASSWORD")

root=tk.Tk()
root.geometry("500x350")
root.title("Login")

user_name=tk.StringVar()
password=tk.StringVar()

tk.Label(root,text="Password:").pack(anchor="w",padx=10,pady=2)
password = tk.Entry(root,show="*")
password.pack(anchor="w",padx=10,pady=2)

submit = tk.Button(root,text="Submit",command=check)
submit.pack(anchor="w",padx=10,pady=2)

root.mainloop()
pass_word=tk.Entry(root)
pass_word.pack(fill="x",padx=10)

tk.Button(root,text="Register",command=register).pack(pady=10)
tk.Button(root,text="Login",command=login).pack(pady=10)

root.mainloop()
