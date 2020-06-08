from tkinter import *

expression=""

def Press(num):
    global expression
    expression =expression+str(num)
    equation.set(expression)

def Pressequal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression=""

def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ =="__main__":
    master = Tk()
    master.title("Calculator")
    master.geometry("270x150")
    master.configure(background = "light green")
    equation= StringVar()
    expression_field = Entry(master,textvariable= equation)
    expression_field.grid(columnspan=4,ipadx=70)
    equation.set("Enter an expression:")

    button1 = Button(master,text="1",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(1))
    button1.grid(row=2,column = 0)
    button2 = Button(master,text="2",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(2))
    button2.grid(row=2,column = 1)
    button3 = Button(master,text="3",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(3))
    button3.grid(row=2,column =2)
    button4 = Button(master,text="4",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(4))
    button4.grid(row=3,column = 0)
    button5 = Button(master,text="5",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(5))
    button5.grid(row=3,column = 1)
    button6 = Button(master,text="6",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(6))
    button6.grid(row=3,column = 2)
    button7 = Button(master,text="7",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(7))
    button7.grid(row=4,column = 0)
    button8 = Button(master,text="8",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(8))
    button8.grid(row=4,column = 1)
    button9 = Button(master,text="9",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(9))
    button9.grid(row=4,column = 2)
    button0 = Button(master,text="0",fg="black",bg="yellow",height=1,width=7,command=lambda:Press(0))
    button0.grid(row=5,column = 1)

    plus= Button(master,text="+",fg="black",bg="yellow",height=1,width=7,command=lambda:Press("+"))
    plus.grid(row=2,column = 3)
    minus= Button(master,text="-",fg="black",bg="yellow",height=1,width=7,command=lambda:Press("-"))
    minus.grid(row=3,column = 3)
    mul= Button(master,text="*",fg="black",bg="yellow",height=1,width=7,command=lambda:Press("*"))
    mul.grid(row=4,column = 3)
    div= Button(master,text="/",fg="black",bg="yellow",height=1,width=7,command=lambda:Press("/"))
    div.grid(row=5,column = 3)
    decimal= Button(master,text=".",fg="black",bg="yellow",height=1,width=7,command=lambda:Press("."))
    decimal.grid(row=5,column = 0)

    equal= Button(master,text="=",fg="white",bg="Blue",height=1,width=7,command=Pressequal)
    equal.grid(row=6,column = 1)
    clear= Button(master,text="C",fg="black",bg="yellow",height=1,width=7,command=clear)
    clear.grid(row=5,column = 2)
    mainloop()
