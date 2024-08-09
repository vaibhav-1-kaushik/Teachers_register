from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


def add() :
      student = Tk()
      student.title("Add students jhada sirha government engineering college")
      student.state("zoomed")

      Roll_no = StringVar()
      N = StringVar()
      B = StringVar()
      Sem = StringVar()

      def Submit():
            Roll = Roll_no.get()
            Name = N.get()
            Branch = B.get()
            Semester = Sem.get()

            if Roll == "" or Name == "" or Branch == "" or Semester == "" or int(Semester) > 8 :
                  messagebox.showinfo(title="oops", message="partially filled the form")
            else:
                  db = pymysql.connect(host="localhost", user="root", password="Vaibhav123@", database="prof")
                  sql = "insert into students values(%s,%s,%s,%s)"
                  value = [Roll, Name, Branch, Semester]

                  cur = db.cursor()
                  cur.execute(sql, value)
                  db.commit()
                  Roll_no.set("")
                  N.set("")
                  B.set("")
                  Sem.set("")


      ttk.Label(student, text="Roll no.").place(x=550, y=150, width=60, height=30)
      ttk.Entry(student, textvariable=Roll_no).place(x=550, y=182, width=200, height=30)

      ttk.Label(student, text="Name").place(x=550, y=214, width=60, height=30)
      ttk.Entry(student, textvariable=N).place(x=550, y=246, width=200, height=30)

      ttk.Label(student, text="Branch").place(x=550, y=278, width=60, height=30)
      ttk.Entry(student, textvariable=B).place(x=550, y=310, width=200, height=30)

      ttk.Label(student, text="Semester").place(x=550, y=345, width=60, height=30)
      ttk.Entry(student, textvariable=Sem).place(x=550, y=380, width=200, height=30)

      ttk.Button(student, text="Save", command=Submit).place(x=550, y=450-30, width=60, height=30)
      student.mainloop()

