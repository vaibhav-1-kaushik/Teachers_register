from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Add_student
import pymysql


def ct() :
     fr_ct = Tk()
     fr_ct.title("Class test Jhada sirha government engineering college")
     fr_ct.state("zoomed")

     roll = StringVar()
     sub = StringVar()
     CT1 = StringVar()
     CT2 = StringVar()

     def sab():
          Roll = roll.get()
          Sub = sub.get()
          C1 = CT1.get()
          C2 = CT2.get()

          if Roll == "" and Sub == "" and C1 == "" and C2 == "":
               messagebox.showinfo(title="oops", message="partially filled the form")
          else:
               db = pymysql.connect(host="localhost", user="root", password="Vaibhav123@", database="prof")
               sql = "insert into class_test values(%s,%s,%s,%s)"
               sql1 = f"select roll_no from students where roll_no = {Roll}"
               value = [Roll, Sub, C1, C2]

               cur = db.cursor()
               # print(cur.execute(sql1))
               if cur.execute(sql1) :
                                     cur.execute(sql, value)
                                     db.commit()
                                     roll.set("")
                                     sub.set("")
                                     CT1.set("")
                                     CT2.set("")
                                     # print(radio1.get())
               else:
                    y = messagebox.askokcancel(title="data not found", message="Press OK to Add student ")
                    if y:
                         Add_student.add()


     # radio1  = StringVar(value="avg")

     ttk.Label(fr_ct, text="Roll no.").place(x=550, y=150, width=60, height=30)
     ttk.Entry(fr_ct, textvariable=roll).place(x=550, y=182, width=200, height=30)

     ttk.Label(fr_ct, text="Subject").place(x=550, y=214, width=60, height=30)
     ttk.Entry(fr_ct, textvariable=sub).place(x=550, y=246, width=200, height=30)

     ttk.Label(fr_ct, text="Marks ct 1").place(x=550, y=278, width=60, height=30)
     ttk.Entry(fr_ct, textvariable=CT1).place(x=550, y=310, width=200, height=30)

     ttk.Label(fr_ct, text="Marks ct 2").place(x=550, y=345, width=60, height=30)
     ttk.Entry(fr_ct, textvariable=CT2).place(x=550, y=380, width=200, height=30)

     # ttk.Radiobutton(fr_ct,text="Average",variable=radio1,value="avg").place(x=550, y=415, width=65, height=30)
     # ttk.Radiobutton(fr_ct,text="Best of",variable=radio1,value="Best of").place(x=625, y=415, width=60, height=30)

     ttk.Button(fr_ct, text="Save", command=sab).place(x=550, y=450, width=60, height=30)

     fr_ct.mainloop()





