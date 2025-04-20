import sqlite3
conn = sqlite3.connect("user.db")
cur = conn.cursor()

cur.execute("create table if not exists user(id integer primary key autoincrement, name text not null,email text unique not null, age integer not null)")

conn.commit()

def add_user():
    name = input("Enter Name : ")
    email = input("Enter Email : ")
    age = input("Enter Age : ")
    
    try:
        cur.execute("insert into user(name,email,age) values(?,?,?)",(name,email,age))
        conn.commit()
        print("User added successfully")
    except sqlite3.IntegrityError:
        print("Error: Email already exists!")
        
def show_user():
    cur.execute("select * from user")
    users = cur.fetchall()
    
    if users:
        print("\nList of Users")
        
        print(f"{'User ID':<10}{'Name':<20}{'Email':<20}{'Age':<3}")
        print("="*52)
        for user in users:
            print(f"{user[0]:<10}{user[1]:<20}{user[2]:<20}{user[3]:<3}")
    else:
        print("No users found")
        
def update_user():
    user_id=input("Enter User ID to update : ")
    cur.execute("select * from user where id = ?",(user_id,))
    user = cur.fetchone()

    if user:
        try:
            new_name = input(f"Enter New Name ({user[1]}) : ")
            new_email = input(f"Enter New Email ({user[2]}) : ")
            new_age = input(f"Enter New Age ({user[3]}) : ")
            cur.execute("update user set name = ?, email = ?,age = ? where id=?",(new_name,new_email,new_age,user_id) )
            conn.commit()
            print("User added successfully")
        except sqlite3.IntegrityError:
            print("Error: Email already exists!")
    else:
        print("User not found")
        
def delete_user():
    user_id=input("Enter User ID to update : ")
    cur.execute("select * from user where id = ?",(user_id,))
    user = cur.fetchone()

    if user:
        cur.execute("delete from user where id=?",(user_id,))
        conn.commit()
        print("User deleted successfully")
    else:
        print("User not found")

while True:
    print("\n C R U D- Database Operations")
    print("1.Add User")
    print("2.Display User")
    print("3.Update User")
    print("4.Delete User")
    print("5.Exit")
    c = input("Enter your choice : ")
    if c == '1':
        add_user()
    elif c == '2':
        show_user()
    elif c == '3':
        update_user()
    elif c == '4':
        delete_user()
    elif c == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid Choice")
conn.close()
