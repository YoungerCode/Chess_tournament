import tkinter
from tkinter import *

#design Main Frame/Screen

def main_account_screen():

    main_screen = Tk()      # creating a GUI window
    main_screen.geometry('200x150') #set the size of GUI window
    main_screen.title('Account Login')      # set title of GUI

#Create a form label
Label(text = 'Choose to Login Or Register', bg ='dark green', width ='300', height = '2',
    font = ('Calibri',13)).pack()

#Create Login Button
Button(text = 'Login', height ='2', width ='30').pack()
Label(text = '').pack()

#Create a register button
Button(text = 'Register', height ='2', width = '30').pack()


main_screen = Tk()      # creating a GUI window
main_screen.geometry('200x150') #set the size of GUI window
main_screen.title('Account Login')

main_screen.mainloop()  #Start The GUI

main_account_screen()   #call the main functiom
