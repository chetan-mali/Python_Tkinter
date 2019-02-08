import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu

win=tkinter.Tk()
win.title("Tic-Tac-Toe")
lst =[" "," "," "," "," "," "," "," "," "]
counter=0
flag =0
def check():
            global flag
            if lst[0]==lst[1]==lst[2]=='X':
                    flag = 1
            elif lst[3]==lst[4]==lst[5]=='X':
                     flag = 1
            elif lst[6]==lst[7]==lst[8]=='X':
                     flag = 1
            elif lst[0]==lst[3]==lst[6]=='X':
                     flag = 1
            elif lst[1]==lst[4]==lst[7]=='X':
                    flag = 1
            elif lst[2]==lst[5]==lst[8]=='X':
                    flag = 1
            elif lst[0]==lst[4]==lst[8]=='X':
                flag = 1
            elif lst[2]==lst[4]==lst[6]=='X':
                    flag = 1
            elif lst[0]==lst[1]==lst[2]=='O':
                    flag = 2
            elif lst[3]==lst[4]==lst[5]=='O':
                     flag = 2
            elif lst[6]==lst[7]==lst[8]=='O':
                     flag = 2
            elif lst[0]==lst[3]==lst[6]=='O':
                     flag = 2
            elif lst[1]==lst[4]==lst[7]=='O':
                    flag = 2
            elif lst[2]==lst[5]==lst[8]=='O':
                    flag = 2
            elif lst[0]==lst[4]==lst[8]=='O':
                flag = 2
            elif lst[2]==lst[4]==lst[6]=='O':
                    flag = 2
            if flag==1:
                messagebox.showinfo("Hey","---- X Player Win ----")
                clear()
            elif flag==2:
                messagebox.showinfo("Hey","---- O Player Win ----")
                clear()
            elif counter==9:
                messagebox.showinfo("OOps!!","---- Match Draw ----")
                    
def B1():
    global counter
    if lst[0]==" ":
        if counter%2==0:
            lst[0]="X"
        else:
            lst[0]="O"
        counter+=1
    button1.configure(text=lst[0])
    check()
def B2():
    global counter
    if lst[1]==" ":
        if counter%2==0:
            lst[1]="X"
        else:
            lst[1]="O"
        counter+=1
    button2.configure(text=lst[1])
    check()
def B3():
    global counter
    if lst[2]==" ":
        if counter%2==0:
            lst[2]="X"
        else:
            lst[2]="O"
        counter+=1
    button3.configure(text=lst[2])
    check()
def B4():
    global counter
    if lst[3]==" ":
        if counter%2==0:
            lst[3]="X"
        else:
            lst[3]="O"
        counter+=1
    button4.configure(text=lst[3])
    check()
def B5():
    global counter
    if lst[4]==" ":
        if counter%2==0:
            lst[4]="X"
        else:
            lst[4]="O"
        counter+=1
    button5.configure(text=lst[4])
    check()
def B6():
    global counter
    if lst[5]==" ":
        if counter%2==0:
            lst[5]="X"
        else:
            lst[5]="O"
        counter+=1
    button6.configure(text=lst[5])
    check()
def B7():
    global counter
    if lst[6]==" ":
        if counter%2==0:
            lst[6]="X"
        else:
            lst[6]="O"
        counter+=1
    button7.configure(text=lst[6])
    check()
def B8():
    global counter
    if lst[7]==" ":
        if counter%2==0:
            lst[7]="X"
        else:
            lst[7]="O"
        counter+=1
    button8.configure(text=lst[7])
    check()
def B9():
    global counter
    if lst[8]==" ":
        if counter%2==0:
            lst[8]="X"
        else:
            lst[8]="O"
        counter+=1
    button9.configure(text=lst[8])
    check()

def clear():
    global flag
    global lst
    global counter
    lst =[" "," "," "," "," "," "," "," "," "]
    button1.configure(text=lst[0])
    button2.configure(text=lst[1])
    button3.configure(text=lst[2])
    button4.configure(text=lst[3])
    button5.configure(text=lst[4])
    button6.configure(text=lst[5])
    button7.configure(text=lst[6])
    button8.configure(text=lst[7])
    button9.configure(text=lst[8])
    counter=0
    flag=0
    
def _quit():
    win.destroy()
    exit()
def about():
    messagebox.showinfo("About","Developed By Chetan Mali & Purushottam Rathore")
#creating a menu bar......
menubar = Menu(win)

# create a pulldown menu, and add it to the menu bar

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=clear)                                     #filemenu
filemenu.add_command(label="Exit", command=_quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About",command=about)                             #helpmenu
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
win.config(menu=menubar)

#win.geometry("500x500+500+100")
button1 = tkinter.Button(win, width=4,height=3,text=lst[0], activebackground="light blue" ,command=B1)
button1.grid(row=0, column=0)

button2 = tkinter.Button(win,width=4,height=3, text=lst[1], activebackground="light blue",command=B2)
button2.grid(row=0, column=1)

button3 = tkinter.Button(win, width=4,height=3,text=lst[2], activebackground="light blue",command=B3)
button3.grid(row=0, column=2)

button4 = tkinter.Button(win, width=4,height=3,text=lst[3], activebackground="light blue",command=B4)
button4.grid(row=1, column=0)

button5 = tkinter.Button(win, width=4,height=3,text=lst[4], activebackground="light blue",command=B5)
button5.grid(row=1, column=1)

button6 = tkinter.Button(win, width=4,height=3,text=lst[5], activebackground="light blue",command=B6)
button6.grid(row=1, column=2)

button7 = tkinter.Button(win,width=4,height=3, text=lst[6], activebackground="light blue",command=B7)
button7.grid(row=2, column=0)

button8 = tkinter.Button(win, width=4,height=3,text=lst[7], activebackground="light blue",command=B8)
button8.grid(row=2, column=1)

button9 = tkinter.Button(win, width=4,height=3,text=lst[8], activebackground="light blue",command=B9)
button9.grid(row=2, column=2)

win.mainloop()
