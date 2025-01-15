import csv
import re
from tkinter import *
from tkinter import messagebox
import os

class Register(Frame):
    def __init__(self, master, show_login_callback):
        super().__init__(master)
        self.show_login_callback = show_login_callback

        self.id_label = Label(self, text="ID")
        self.id_label.pack()
        self.id_entry = Entry(self)
        self.id_entry.pack()

        self.username_label = Label(self, text="Username")
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

        self.password_strength_label = Label(self, text="")
        self.password_strength_label.pack()

        self.password_requirements = Label(
            self,
            text="Password must contain:\n- At least 8 characters\n- One uppercase letter\n- One lowercase letter\n- One number\n- One special character",
            justify=LEFT,
        )
        self.password_requirements.pack()

        self.confirm_password_label = Label(self, text="Confirm Password")
        self.confirm_password_label.pack()
        self.confirm_password_entry = Entry(self, show="*")
        self.confirm_password_entry.pack()

        self.register_button = Button(self, text="Register", command=self.register_user)
        self.register_button.pack()

        self.back_to_login_button = Button(self, text="Back to Login", command=self.show_login_callback)
        self.back_to_login_button.pack()

        self.password_entry.bind("<KeyRelease>", self.check_password_strength)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
            self.confirm_password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            self.confirm_password_entry.config(show="*")

    def check_password_strength(self, event=None):
        password = self.password_entry.get()

        has_length = len(password) >= 8
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

        if all([has_length, has_upper, has_lower, has_digit, has_special]):
            self.password_strength_label.config(text="Strong Password ✓", fg="green")
        elif has_length and sum([has_upper, has_lower, has_digit, has_special]) >= 3:
            self.password_strength_label.config(text="Moderate Password", fg="orange")
        else:
            self.password_strength_label.config(text="Weak Password", fg="red")

    def register_user(self):
        user_id = self.id_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not all([user_id, username, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if len(password) < 8:
            messagebox.showerror("Invalid Password", "Password must be at least 8 characters long")
            return
        if not re.search(r'[A-Z]', password):
            messagebox.showerror("Invalid Password", "Password must contain at least one uppercase letter")
            return
        if not re.search(r'[a-z]', password):
            messagebox.showerror("Invalid Password", "Password must contain at least one lowercase letter")
            return
        if not re.search(r'\d', password):
            messagebox.showerror("Invalid Password", "Password must contain at least one number")
            return
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messagebox.showerror("Invalid Password", "Password must contain at least one special character")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        file_path = "C:\\AVANTEL_INTERNSHIP\\abc\\tkinter-login-app\\src\\data\\user1.csv"

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Username", "Password"])

        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row and (row[0] == user_id or row[1] == username):
                    messagebox.showerror("Error", "User ID or username already exists")
                    return

        try:
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_id, username, password])

            self.id_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.confirm_password_entry.delete(0, END)
            self.password_strength_label.config(text="")

            messagebox.showinfo("Success", "Registration successful!\nYou can now log in with your credentials.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while registering: {str(e)}")
            return