from tkinter import *
from tkinter import ttk
import registration
import prof_login


page = Tk()
page.title("Jhada sirha government engineering college")
page.state("zoomed")

def cl() :
     page.destroy()
     registration.regi()

def cl2() :
     page.destroy()
     prof_login.prolog()





ttk.Label(text="Jhada sirha government engineering college").place(x=500,y=40,width=200,height=50)
ttk.Button(text="REGISTER NOW",command=cl).place(x=500,y=100,width=200,height=100)
ttk.Button(text="LOGIN NOW",command=cl2).place(x=500,y=250,width=200,height=100)

page.mainloop()