from tkinter import *
from tkinter import messagebox
import csv
import os

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.username_label = Label(master, text="Username")
        self.username_label.pack()

        self.username_entry = Entry(master)
        self.username_entry.pack()

        self.password_label = Label(master, text="Password")
        self.password_label.pack()

        self.password_entry = Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = Button(master, text="Register", command=self.go_to_registration)
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.verify_credentials(username, password):
            messagebox.showinfo("Login Successful", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def verify_credentials(self, username, password):
        if not os.path.exists('data/users.csv'):
            return False
        with open('data/users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False

    def go_to_registration(self):
        self.master.destroy()
        import registration
        root = Tk()
        registration.Registration(root)
        root.mainloop()