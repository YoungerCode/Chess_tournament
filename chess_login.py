import Tkinter
from Tkinter import *
#import Tkinter.messagebox
from tkinter.messagebox import *


class LoginFrame(Frame):

    def _init_(self, master):
        super()._init_(master)

        self.label_username = Label(self, text = 'Username')
        self.label_password = Label(self, text = 'Password')
