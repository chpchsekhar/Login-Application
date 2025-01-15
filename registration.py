from tkinter import *
import csv
import os

class Registration:
    def __init__(self, master):
        self.master = master
        master.title("User Registration")

        self.label_username = Label(master, text="Username")
        self.label_username.pack()

        self.entry_username = Entry(master)
        self.entry_username.pack()

        self.label_password = Label(master, text="Password")
        self.label_password.pack()

        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        self.register_button = Button(master, text="Register", command=self.register)
        self.register_button.pack()

        self.message = Label(master, text="", fg="red")
        self.message.pack()

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.username_exists(username):
            self.message.config(text="Username already exists.")
        else:
            self.save_user_data(username, password)
            self.message.config(text="Registration successful!")

    def username_exists(self, username):
        if not os.path.isfile('data/users.csv'):
            return False
        with open('data/users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return True
        return False

    def save_user_data(self, username, password):
        with open('data/users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])