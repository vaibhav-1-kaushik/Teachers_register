from tkinter import *
from tkinter import ttk
import Add_student
import class_test
import dis_student

def onlogin():
     sec = Tk()
     sec.title("prof section jhada sirha government engineering college")
     sec.state("zoomed")

     def Ads() :
           sec.destroy()
           Add_student.add()

     def CT() :
           sec.destroy()
           class_test.ct()

     def results() :
          sec.destroy()
          dis_student.res()

     ttk.Button(sec,text="Add student",command=Ads).place(x=550,y=200,width=150,height=50)
     ttk.Button(sec, text="Class test (CT)",command=CT).place(x=550, y=255, width=150, height=50)
     ttk.Button(sec, text="Results",command=results).place(x=550, y=310, width=150, height=50)

     sec.mainloop()

