import tkinter
from tkinter import *

####################################### Defining Verification function


def login_verify():
#get username and password

    username1 = username_verify.get()
    password1 = password_verify.get()
# this will delete the entry after login button is pressed
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

#The method listdir() returns a list containing the names of the entries in the directory given by path.
    list_of_files = os.listdir()

#defining verification's conditions
    if username1 in list_of_files:
        file1 = open(username1, "r")   # open the file in read mode

#read the file,
#as splitlines() actually splits on the newline character,
#the newline character is not left hanging at the end of each line. if password1 in verify:

        verify = file1.read().splitlines()
           login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

############################################# Designing Login Success Popup

def login_sucess():

    global login_success_screen   # make login_success_screen global
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()

# create OK button
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def delete_login_success():
    login_success_screen.destroy()

############################################## Designing Invalid Password Popup

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# And now define a function for deleting this popup.

def delete_password_not_recognised():
    password_not_recog_screen.destroy()


############################################### Designing User Not Found Popup

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Now define a function for deleting this popup.

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
