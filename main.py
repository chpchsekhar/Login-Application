from tkinter import *
from login_view import Login
from register import Register
from home import Home

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("User Login and Registration")
        self.master.geometry("400x300")

        self.show_login()

    def show_login(self):
        self.clear_frame()
        self.login_frame = Login(self.master, self.show_register, self.show_home)
        self.login_frame.pack()

    def show_register(self):
        self.clear_frame()
        self.register_frame = Register(self.master, self.show_login)
        self.register_frame.pack()

    def show_home(self):
        self.clear_frame()
        self.home_frame = Home(self.master, self.show_login)
        self.home_frame.pack()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    try:
        root = Tk()
        app = MainApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
