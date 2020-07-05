############################# working on the save button#########################
import Tkinter
from Tkinter import * 


root = Tk()

Label(root, text = "User Name  ").grid (row = 0, sticky = W)
Label(root, text = "Cohort Number ").grid(row = 1, sticky = W)
Label(root, text = "Department").grid(row = 2, sticky = W)
Label(root, text = "")

Uname = Entry(root)
Conum = Entry(root)
Dep   = Entry(root)

Uname.grid(row = 0, column = 1)
Conum.grid(row = 1, column = 1)
Dep.grid(row = 3, column = 1)

def getInput():

    u = Uname.get()
    c = Conum.get()
    d = Dep.get()
    root.distroy()

    global params
    params = [u,c,d]

Button(root, text = "submit",
            command = getInput).grid(row = 5, sticky = W)

            print(params)

mainloop()

#print(params)
