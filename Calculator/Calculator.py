"""
Created on Thu Feb  7 19:36:17 2019


@author: Chetan Mali


testing
"""
from tkinter import messagebox 
from tkinter import *
from tkinter import Menu
from tkinter import font
import tkinter 
win=tkinter.Tk()

win.resizable(width=False, height=False)
win.title("Calculator")
win.geometry("215x355+400+400")
Input =StringVar()
flag=0
def clear():
    Enterybox.delete('0.0', END)
def Back():
    x=Enterybox.get('0.0',END)
    Enterybox.delete('0.0',END)
    x=x[:-2]
    print(x)
    Enterybox.insert(END,x)
def operation():
    global flag
    query=Enterybox.get('0.0',END)
    try:
        Enterybox.delete('0.0', END)
        Enterybox.insert(END, eval(query))
    except:    
        Enterybox.delete('0.0', END)
        Enterybox.insert(END, "invalid input")
        flag=1
def inputfrombutton(num):
    #Enterybox.delete(0, END) #deletes the current value
    global flag
    if num=="=":
        operation()
    elif num=="C":
        clear()
    elif num=="B":
        Back()
    else:
        if flag==1:
            Enterybox.delete('1.0',END)
            Enterybox.insert(END, num)
            flag=0
        else:
            Enterybox.insert(END, num)
def about():
    messagebox.showinfo("About","DeVeloped by Chetan Mali")
            
menubar = Menu(win)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="Developer",command=about)
menubar.add_cascade(label="About",menu=helpmenu)

win.config(menu=menubar)
"""
Enterybox = tkinter.Entry(win,textvariable=Input,width=28,justify="right",bd=5,selectborderwidth=20)
Enterybox.place(x=2,y=0)
"""
bvar1 = font.Font(weight='bold',size=10)
Enterybox = tkinter.Text(win,width=29,height=3,font=bvar1)
Enterybox.place(x=3,y=0)

bvar = font.Font(weight='bold')
B1 = tkinter.Button(win,text="C",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="red",font=bvar,command=lambda: inputfrombutton("C"))
B1.place(x=2,y=47)
B2 = tkinter.Button(win,text="B",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("B"))
B2.place(x=55,y=47)
B3 = tkinter.Button(win,text="%",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("%"))
B3.place(x=107,y=47)
B4 = tkinter.Button(win,text="/",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("/"))
B4.place(x=160,y=47)
B5 = tkinter.Button(win,text="7",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("7"))
B5.place(x=2,y=98)
B6 = tkinter.Button(win,text="8",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("8"))
B6.place(x=55,y=98)
B7 = tkinter.Button(win,text="9",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("9"))
B7.place(x=107,y=98)
B8 = tkinter.Button(win,text="x",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("*"))
B8.place(x=160,y=98)
B9 = tkinter.Button(win,text="4",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("4"))
B9.place(x=2,y=147)
B10 = tkinter.Button(win,text="5",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("5"))
B10.place(x=55,y=147)
B11 = tkinter.Button(win,text="6",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("6"))
B11.place(x=107,y=147)
B12 = tkinter.Button(win,text="-",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("-"))
B12.place(x=160,y=147)
B13 = tkinter.Button(win,text="1",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("1"))
B13.place(x=2,y=197)
B14 = tkinter.Button(win,text="2",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("2"))
B14.place(x=55,y=197)
B15 = tkinter.Button(win,text="3",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("3"))
B15.place(x=107,y=197)
B16 = tkinter.Button(win,text="+",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("+"))
B16.place(x=160,y=197)
B17 = tkinter.Button(win,text=".",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("."))
B17.place(x=2,y=247)
B18 = tkinter.Button(win,text="0",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("0"))
B18.place(x=55,y=247)
B19 = tkinter.Button(win,text="(",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton("("))
B19.place(x=107,y=247)
B20 = tkinter.Button(win,text=")",width=2,height=2,activebackground="lightblue",bd=4,bg="gray26",
                    fg="white",font=bvar,command=lambda: inputfrombutton(")"))
B20.place(x=160,y=247)
B21 = tkinter.Button(win,text="=",width=17,height=2,activebackground="lightblue",bd=4,bg="chocolate3",
                    fg="white",font=bvar,command=lambda: inputfrombutton("="))
B21.place(x=5,y=300)

win.mainloop()
