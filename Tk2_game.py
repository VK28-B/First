from tkinter import *
import random
root=Tk()
root.geometry("600x320+400+100")
root.resizable(False,False)
root.title('GUSS THE NUMBER GAME')
root.config(bg="white")
y=260
num_of_you = IntVar()
def xyz(event=""):
    cbdbjdc=Label(text="ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc", fg="white", bg="white").place(x=150, y=0)
    s=random.randrange(1,100)
    def getvals(event=''):
     if num_of_you.get()=="":
        num_of_you.set("")
        l1=Label(text="Please put a valid number", fg="red", font=("bold"), bg="white").place(x=200,y=y)
     elif num_of_you.get()==s:
        l1=Label(text="yes, you gussed it right!", fg="red", font=("bold"), bg="white").place(x=200,y=y)
        root.bind('<Shift-">' , xyz)
        ok2=Button(root, text="NEXT", border=15, relief=GROOVE , command=xyz).place(x=280,y=200)
     elif num_of_you.get()>s:
        l2=Label(text='choose smaller number', font=(20), bg="white").place(x=202,y=y)
        ok255=Label(root, text="NEXT", bg="white").place(x=210,y=200, width=2020, height=55)
        num_of_you.set("")
     elif num_of_you.get()<s:
        l3=Label(text="   choose bigger number", font=(20), bg="white").place(x=202,y=y, width=210)
        ok255=Label(root, text="NEXT", bg="white").place(x=210,y=200, width=2020, height=55)
        num_of_you.set("")
     
    head=Label(root, text="Enter The Num. Less Than 100", font=("times new roman",30,"italic", "bold"),bg="white", fg="blue", bd=15, relief=GROOVE).place(x=30,y=10)
    Entry(root, fg="red" , textvariable=num_of_you).place(x=250,y=100)
    root.bind('<Control-m>' , getvals)
    ok=Button(root, text="OK", border=15, relief=GROOVE , command=getvals).place(x=285, y=140)
    num_of_you.set("")
button0303030=Button(text="GUSS THE NUM", command=xyz).pack()

root.mainloop()