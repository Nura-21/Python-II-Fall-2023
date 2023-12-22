import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='admin',
            password='admin',
            database='python'
        )
        return connection
    except Error as e:
        print("Error while SQL query: ", e)
        return None

def add_user_to_db():
    username = username_entry.get()
    password = password_entry.get()
    connection = create_db_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            messagebox.showinfo("Success", "User was successfully added to database")
        except Error as e:
            print("Error while SQL query: ", e)
        finally:
            connection.close()

def show_users_from_db():
    connection = create_db_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            user_listbox.delete(0, tk.END)
            for row in result:
                user_listbox.insert(tk.END, f"Username: {row[0]}, Password: {row[1]}")
        except Error as e:
            print("Error while SQL query: ", e)
        finally:
            connection.close()

root = tk.Tk()
root.title("MySQL and Tkinter")
root.geometry('500x500')
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

username_label = tk.Label(frame, text="Name: ")
username_label.pack()

username_entry = tk.Entry(frame)
username_entry.pack()

password_label = tk.Label(frame, text="Password: ")
password_label.pack()

password_entry = tk.Entry(frame)
password_entry.pack()

add_button = tk.Button(frame, text="Add user", command=add_user_to_db)
add_button.pack()

show_button = tk.Button(frame, text="Show users", command=show_users_from_db)
show_button.pack()

user_listbox = tk.Listbox(frame)
user_listbox.pack()

root.mainloop()