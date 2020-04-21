import tkinter
from tkinter import *
#import Tkinter.messagebox
from tkinter.messagebox import *
import tkinter.messagebox as tm


class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text = 'Username')
        self.label_password = Label(self, text = 'Password')

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show = '*')

        self.label_username.grid(row=0, sticky = E)
        self.label_password.grid(row=1, sticky = E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text ='keep me logged in' )
        self.checkbox.grid(columnspan = 2)

        self.logbtn = Button(self, text = 'Login', command = self.login_button_clicked )
        self.logbtn.grid(columnspan = 2)

        self.pack()

    def login_button_clicked(self):
        #print(clicked)
        username = self.entry_username.get()
        password = self.entry_password.get()

        #print(ussername, password)

        if username == 'mahnatse' and password == 'password':
            tm.showinfo('Login info', 'Welcome Mahnatse')
        else:
            tm.showerror('Login error', 'Inccorect username')


root = Tk()
lf = LoginFrame(root)
root.mainloop()
