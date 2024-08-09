from tkinter import *
from tkinter import  ttk
from tkinter import  messagebox
import prof_login
import pymysql



def regi() :
    reg = Tk()
    reg.title("Registration page Jhada sirha government engineering college")
    reg.state("zoomed")
    id = StringVar()
    name = StringVar()
    phone = StringVar()
    pasw = StringVar()
    # ver = StringVar()
    #---->>methods<<-----
    def save() :
         ID = id.get()
         Name = name.get()
         pho = phone.get()
         pw = pasw.get()

         if ID == "" and Name =="" and pho =="" and pw=="":
                              messagebox.showinfo(title="oops",message="partially filled the form")
         else:
             db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="prof")
             sql = "insert into register values(%s,%s,%s,%s)"
             value = [ID,Name,pho,pw]

             cur = db.cursor()
             if cur.execute(sql,value) :
                            db.commit()
                            id.set("")
                            name.set("")
                            phone.set("")
                            pasw.set("")
                            reg.destroy()
                            prof_login.prolog()

    # return save()

    ttk.Label(reg, text="ID").place(x=550, y=150, width=60, height=30)
    ttk.Entry(reg, textvariable=id).place(x=550, y=182, width=200, height=30)

    ttk.Label(reg, text="Name").place(x=550, y=214, width=60, height=30)
    ttk.Entry(reg, textvariable=name).place(x=550, y=246, width=200, height=30)

    ttk.Label(reg, text="Mobile no.").place(x=550, y=278, width=60, height=30)
    ttk.Entry(reg, textvariable=phone).place(x=550, y=310, width=200, height=30)

    ttk.Label(reg, text="password").place(x=550, y=342, width=60, height=30)
    ttk.Entry(reg, textvariable=pasw).place(x=550, y=374, width=200, height=30)

    ttk.Button(reg, text="Save", command=save).place(x=550, y=410, width=60, height=30)


    reg.mainloop()




