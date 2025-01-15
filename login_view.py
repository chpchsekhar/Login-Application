import csv
from tkinter import *
from tkinter import messagebox
import os

class Login(Frame):
    def __init__(self, master, show_register_callback, show_home_callback):
        super().__init__(master)
        self.show_register_callback = show_register_callback
        self.show_home_callback = show_home_callback

        # Username (ID) Label and Entry
        self.username_label = Label(self, text="ID")
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        # Password Label and Entry
        self.password_label = Label(self, text="Password")
        self.password_label.pack()

        self.password_entry = Entry(self, show="*")
        self.password_entry.pack()

        # Show Password Checkbox
        self.show_password_var = IntVar()
        self.show_password_check = Checkbutton(
            self, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility
        )
        self.show_password_check.pack()

        # Login Button
        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.pack()

        # Register Button
        self.register_button = Button(self, text="Register", command=self.show_register_callback)
        self.register_button.pack()

        # Message Label
        self.message_label = Label(self, text="")
        self.message_label.pack()

    def toggle_password_visibility(self):
        # Toggle Password Visibility
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        user_id = self.username_entry.get().strip()  # Remove extra spaces from the input
        password = self.password_entry.get().strip()

        # Path to the CSV file
        file_path ="C:\\AVANTEL_INTERNSHIP\\abc\\tkinter-login-app\\src\\data\\users.csv"
        if os.path.exists(file_path):  # Check if the file exists
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)  # Read CSV rows
                for row in reader:  # Iterate through rows
                    if len(row) >= 3:  # Ensure row has at least 3 columns
                        csv_id = row[0].strip()  # Get and strip ID
                        csv_password = row[2].strip()  # Get and strip password

                        # Compare input with CSV data
                        if csv_id == user_id and csv_password == password:
                            messagebox.showinfo("Success", "Login successful!")
                            self.show_home_callback()  # Redirect to home page
                            return

        # If no match is found
        messagebox.showerror("Error", "Invalid credentials.")
