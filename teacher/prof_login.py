from tkinter import *
from tkinter import ttk
import pymysql
import prof_section
from tkinter import  messagebox


def prolog():
    log = Tk()
    log.title("Login page Jhada sirha government engineering college")
    log.state("zoomed")
    uid = StringVar()
    upw = StringVar()
    def cl3() :
         log.destroy()
         prof_section.onlogin()

    def verify() :
         db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="prof")
         sql = f"select * from register where u_id = {uid.get()} and password = {upw.get()};"

         cur = db.cursor()
         if cur.execute(sql) :
                       f = cur.fetchall()
                       if f[0][3]==upw.get() :
                               messagebox.showinfo(title="success",message="login successfully")
                               cl3()
         else :
               messagebox.showwarning(title="notice",message="invalid details, data not found")


    ttk.Label(log, text="ID").place(x=550, y=150, width=60, height=30)
    ttk.Entry(log, textvariable=uid).place(x=550, y=182, width=200, height=30)

    ttk.Label(log, text="Password").place(x=550, y=214, width=60, height=30)
    ttk.Entry(log, textvariable=upw).place(x=550, y=246, width=200, height=30)



    ttk.Button(log,text="Login",command=verify).place(x=550, y=280, width=60, height=30)

    log.mainloop()
