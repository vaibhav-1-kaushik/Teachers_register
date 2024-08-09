from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


def res() :
    dis = Tk()
    dis.title("Result section jhada sirha government engineering college")
    dis.state("zoomed")

    r = StringVar()
    N = StringVar()
    M = StringVar()

    def on_submit():

        db = pymysql.connect(host="localhost", user="root", password="Vaibhav123@", database="prof")
        sql = f"select students.roll_no,students.name,Avg((class_test.CT1+class_test.CT2)/2) as avg_marks from class_test inner join students on students.roll_no = class_test.roll_no where students.roll_no ={r.get()} group by students.roll_no,students.name; ;"

        cur = db.cursor()

        if cur.execute(sql):
            for f in cur.fetchall():
                v.delete(0,END)
                q.delete(0,END)
                v.insert(1, f[1])
                q.insert(1, f[2])
        else:
            v.delete(0,END)
            q.delete(0,END)
            messagebox.showinfo(title="something wrong", message="data not available")

            # r.set("")
            # N.set("")
            # M.set("")

    ttk.Label(dis, text="Roll no.").place(x=550, y=150, width=50, height=30)
    ttk.Label(dis, text=":").place(x=610, y=150, width=10, height=30)
    ttk.Entry(dis, textvariable=r).place(x=622, y=150, width=150, height=30)

    ttk.Button(dis, text="submit", command=on_submit).place(x=774, y=150, width=70, height=30)

    ttk.Label(dis, text="Name").place(x=550, y=182, width=50, height=30)
    ttk.Label(dis, text=":").place(x=610, y=182, width=10, height=30)
    v = ttk.Entry(dis, textvariable=N)
    v.place(x=622, y=182, width=150, height=30)

    ttk.Label(dis, text="Marks").place(x=550, y=214, width=50, height=30)
    ttk.Label(dis, text=":").place(x=610, y=214, width=10, height=30)
    q = ttk.Entry(dis, textvariable=M)
    q.place(x=622, y=214, width=150, height=30)


    dis.mainloop()
