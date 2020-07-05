#import tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk
import random
from datetime import datetime
#import Tk.MessageBox


# In[ ]:


class Tournament:

    def __init__(self, root):
        self.root = root
        self.root.title("Chess Tournament System")
        #self.root.geometry("1350+750+0+0")
        self.root.configure(background = "black")

        ########################################### Frames #######################################################

        Mainframe = Frame(self.root)
        Mainframe .grid()

        Titleframe = Frame(Mainframe,width = 150,padx=20,bd=20,relief = RIDGE)
        Titleframe.pack(side = TOP)

        self.lblTitle = Label(Titleframe,width = 39,font = ('arial',40,'bold'),text = "\tChess Tournament\t",padx =12)
        self.lblTitle .grid()

        Dataframe = Frame(Mainframe, bd = 20, width =100, height = 200, padx = 20, relief = RIDGE)
        Dataframe.pack(side=BOTTOM)


        Dataframeleft = LabelFrame(Dataframe, bd = 10 ,width = 350,height = 600, padx = 20, relief=RIDGE, font=('arial', 12, 'italic', 'bold'), text = "\tPlayer Details\t",)
        Dataframeleft.pack(side = LEFT)

        Dataframeright = LabelFrame(Dataframe, bd = 10 ,width = 350,height = 600, padx = 20, relief=RIDGE, font=('arial', 12, 'italic', 'bold'), text = "\tList of Players\t",)
        Dataframeright.pack(side = RIGHT)


        ########################################### Widget/s ############################################################

        self.lblUsername = Label(Dataframeleft, font =('arial', 12, 'bold'), text = "Username: ", padx=2, pady=2)
        self.lblUsername .grid(row=0, column=0, sticky=W)
        self.lblName = Entry(Dataframeleft, font=('arial', 12, 'bold'), width =25)
        self.lblName .grid(row=0, column=1)

        self.lblName = Label(Dataframeleft, font =('arial', 12, 'bold'), text = "Name: ", padx=2, pady=2)
        self.lblName .grid(row=1, column=0, sticky=W)
        self.lblName = Entry(Dataframeleft, font=('arial', 12, 'bold'), width =25)
        self.lblName .grid(row=1, column=1)


        self.lblCohort = Label(Dataframeleft, font =('arial', 12, 'bold'), text = "Cohort: ", padx=2, pady=2)
        self.lblCohort .grid(row=2, column=0, sticky=W)

        self.cboCohort = ttk.Combobox(Dataframeleft, font =('arial', 12, 'bold'), state ='readonly', width =23)
        self.cboCohort['value'] = ('','14', '15', '16', '17', '18', '19', '20', '21', 'Staff')
        self.cboCohort.current(0)
        self.cboCohort .grid(row=2, column=1)


        self.lblLevel = Label(Dataframeleft, font =('arial', 12, 'bold'), text = "Level of Experience: ", padx=2, pady=2)
        self.lblLevel .grid(row=3, column=0, sticky=W)

        self.cboLevel = ttk.Combobox(Dataframeleft, font =('arial', 12, 'bold'), state ='readonly', width =23)
        self.cboLevel ['value'] = ('','Beginner', 'Novice', 'Master')
        self.cboLevel .current(0)
        self.cboLevel .grid(row=3, column=1)

        ###################################### List of players Widget#############################################
        self.txtDisplayR=Text(Dataframeright,font=('arial', 12, 'bold'), width =32, height=13, padx=8, pady=20)
        self.txtDisplayR.grid(row=0, column=2)

        #####################################List Box ###########################################################
        scrollbar = Scrollbar(Dataframeright)
        scrollbar.grid(row=0, column = 1, sticky='ns')


        ListOfPlayers = ['Tim', 'James', 'Sibu', 'Gloria', 'Nathi', 'Jacquar', 'Danziel', 'Dineo', 'Themba', 'Tumi', 'Senzo',
                        'Sfiso', 'Leheto', 'Rose', 'Joe', 'Sindi', 'Velly', 'John', 'Matthew', 'Donald', 'Obama', 'Thando',
                        'Mbali', 'Pricillia', 'King', 'Keoreketswe', 'Peter', 'London', 'December']

        playerlist = Listbox(Dataframeright, width = 20, height = 12, font = ('arial', 12, 'bold'))
        playerlist.bind('<<ListboxSelect>>')
        playerlist.grid(row=0, column =0, padx =8)
        scrollbar.config(command=playerlist.yview)

        for iteams in ListOfPlayers:
            playerlist.insert(END,iteams)







       # DataframeLeft = Label(Dataframe,bd = 10 ,width = 800,height = 300, padx = 20, relief=RIDGE,font = ('arial',12,'bold'),text = "Player Details",)
        #DataframeLeft.pack(side = "left")

if __name__ == '__main__':
    root =Tk()
    application = Tournament(root)
    root.mainloop()


# In[ ]:





# In[ ]:
