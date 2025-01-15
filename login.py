import csv
from tkinter import *
from tkinter import messagebox
import os

class Login(Frame):
    def __init__(self, master, show_register_callback, show_home_callback):
        super().__init__(master)
        self.show_register_callback = show_register_callback
        self.show_home_callback = show_home_callback

        self.username_label = Label(self, text="ID")
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text="Password")
        self.password_label.pack()

        self.password_entry = Entry(self, show="*")
        self.password_entry.pack()

        self.show_password_var = IntVar()
        self.show_password_check = Checkbutton(
            self, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility
        )
        self.show_password_check.pack()

        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = Button(self, text="Register", command=self.show_register_callback)
        self.register_button.pack()

        self.message_label = Label(self, text="")
        self.message_label.pack()

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        user_id = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        file_path = os.path.join("data", "user1.csv")
        if os.path.exists(file_path):
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 3:
                        csv_id = row[0].strip()
                        csv_password = row[2].strip()

                        if csv_id == user_id and csv_password == password:
                            messagebox.showinfo("Success", "Login successful!")
                            self.show_home_callback()
                            return

        messagebox.showerror("Error", "Invalid credentials.")
