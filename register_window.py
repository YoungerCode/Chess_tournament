import tkinter
from tkinter import *

################## Designing New Screen For Registration
def register():

    register_screen = Toplevel(main_screen)
    register_screen.title('Register')
    register_screen.geometry('300X250')

    #Set text variables
    username = StringVar()
    password = StringVar()

    #label for user's instructions
    Label(register_screen, text = 'Please enter details below', bg='dark orange').pack()

    #Set username label
    username_lable = Label(register_screen, text = 'Username *')
    username_lable.pack()

    #Set username entry
    username_entry = Entry(register_screen, textvariable =username)
    username_entry.pack()

    #Set password label
    password_label = Label(register_screen, test = 'Password *')
    password_label.pack()

    #Set password entry
    password_entry = Entry(register_screen, textvariable = password, show = '*')
    password_entry.pack()

    Label(register_screen, text ='').pack()

    #Set register button
    Button(register_screen, text = 'Register', width = 10,
            height = 1, bg = 'dark red').pack()

global main_screen

# add command = register in button Widget
Button(text ='Register', height = '2', width ='30', command = register).pack()




##################### Assigning Functions To Register Button

def register_user():

    #get username and Password
    username_info = username.get()
    password_info = password.get()

    #open file in write mode
    file = open(username_info, 'w')

    #write username and password info into file
    file.write(username_info + '\n')
    file.write(password_info)
    file.close

    username_entry.delete(0, END)
    password_entry.delete(0, END)

# make a label to show success info on the Screen
Label(register, text = 'Registration Successful', fg ='dark green',
      font =('Calibri', 11)).pack()

# set global variables

global username
global password
global username_entry
global password_entry

# Add comand

Button(register_screen, text = 'Register', width = 10, height =1, bg ='light blue',
        command = 'register_user').pack()

root = Tk()
lf = LoginFrame(root)
root.mainloop()
