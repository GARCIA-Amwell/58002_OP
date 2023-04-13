from tkinter import *
class MyFullName:
  def __init__(self, name):
    self.lbl4 = Label(name, text ="My Full Name")
    self.lbl4.place(x=150, y=50)
    self.lbl1 = Label(name, text = "Enter Given Name: ")
    self.lbl1.place(x=100, y=50)
    self.lbl2 = Label(name, text = "Enter Middle Name: ")
    self.lbl2.place(x=100, y=100)
    self.lbl5 = Label(name, text = "Enter Last Name: ")
    self.flbl5.place(x=100, y=150)
    self.lbl3 = Label(name, text = "My Full Name is: ")
    self.lbl3.place(x=100, y=225)
    self.txt1 = Entry (name,bd=1)
    self.txt1.place(x=200, y=50)
    self.txt2 = Entry (name,bd=2)
    self.txt2.place(x=200, y=100)
    self.txt5 = Entry (name,bd=5)
    self.txt5.place(x=200, y=150)
    self.txt3 = Entry (name,bd=1)
    self.txt3.place(x=200, y=225)
    self.btnfull = Button(name,text = "Show Full Name")

    def full(self,full):
      self.txt3.delete(0,'end')
      GN = int(self.txt1.get())
      MN = int(self.txt2.get())
      LN = int(self.txt5.get())
      full = LN + GN + MN
      self.txt3.insert(END, str(full))

windows = Tk ()
winn = Name(window)
windows.geometry("700x500 + 20 + 20")
window.title("Midterm Exam Problem 2")
window.mainloop()