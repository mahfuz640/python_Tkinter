import tkinter as tk

class LoginForm:
    def __init__(self, master):
        self.master = master
        master.title("Login Form")
        master.geometry('300x150')

        # Create labels and entry fields for username and password
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        # Create a login button
        self.login_button = tk.Button(master, text="Login", command=self.check_credentials)
        self.login_button.pack()

    def check_credentials(self):
        # TO DO: implement login logic here
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Username: {username}, Password: {password}")

root = tk.Tk()
login_form = LoginForm(root)
root.mainloop()