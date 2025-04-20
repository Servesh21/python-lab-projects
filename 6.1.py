import tkinter as tk
from tkinter import ttk, messagebox
import bcrypt
import sqlite3



conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("create table if not exists users ( id integer primary key autoincrement, username text unique not null, email text unique not null, password text not null)")
conn.commit()

def hash_password(password):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    
def check_password(hashed_password,user_password):
    return bcrypt.checkpw(user_password.encode(),hashed_password)
    
def register():
    username = user_name.get()
    email = email_id.get()
    password = pass_word.get()
    
    if not username or not email or not password:
        messagebox.showerror("Error","All fields are compulsory")
        return
    
    if "@" not in email or "." not in email:
        messagebox.showerror("Error","Enter a valid email")
        return
        
    if len(password)<6:
        messagebox.showerror("Error","Password must be atleast 6 characters")
        return
    
    hashed_pass = hash_password(password)
    
    try:
        cur.execute("insert into users (username,email,password) values (?,?,?)",(username,email,hashed_pass))
        conn.commit()
        messagebox.showinfo("Success","Registration Successful! You can log in now")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error","Username or Email already exists")
        
def login():
    username = user_name.get()
    password = pass_word.get()
    
    if not username or not password:
        messagebox.showerror("Error","All fields are required")
        return
        
    cur.execute("select password from users where username = ?",(username,))
    user =cur.fetchone()
    
    if user and check_password(user[0],password):
        messagebox.showinfo("Success","Login Successful! Welcome "+username)
    else:
        messagebox.showerror("Error","Invalid Username or Password!")
    

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

tk.Label(root,text="Password:").pack(anchor="w",padx=10,pady=2)
pass_word=tk.Entry(root)
pass_word.pack(fill="x",padx=10)

tk.Button(root,text="Register",command=register).pack(pady=10)
tk.Button(root,text="Login",command=login).pack(pady=10)

root.mainloop()
