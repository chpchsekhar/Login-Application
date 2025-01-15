from tkinter import Tk, Frame, Button, Label
from registration import Registration
from login import Login

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication App")
        self.root.geometry("300x200")

        self.frame = Frame(self.root)
        self.frame.pack(pady=20)

        self.label = Label(self.frame, text="Welcome to User Auth App")
        self.label.pack()

        self.register_button = Button(self.frame, text="Register", command=self.show_registration)
        self.register_button.pack(pady=5)

        self.login_button = Button(self.frame, text="Login", command=self.show_login)
        self.login_button.pack(pady=5)

    def show_registration(self):
        self.frame.pack_forget()
        self.registration = Registration(self.root)
        
    def show_login(self):
        self.frame.pack_forget()
        self.login = Login(self.root)

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()