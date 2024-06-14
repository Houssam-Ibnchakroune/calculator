'''sceinentific calculator'''
'''first simple like this '''
from tkinter import *
from math import *
window = Tk()
window.geometry("280x525")
var=StringVar()
entry1=Entry(window,textvariable=var,width=23,font=('Arial', 15))
entry1.grid(row=0,column=0,columnspan=4)
entry1.focus_set()   #pour faire le curseur dans cette entry
def ln(x) :
    return log(x)
def button_click(i) :
    entry1.insert(INSERT, str(i))
for i in range(10):
    if i == 0:
        Button(window, text=str(i), width=8,height=4 , command= lambda i=i :button_click(i)).grid(row=7, column=0)
    else:
        Button(window, text=str(i), width=8,height=4 ,command= lambda i=i : button_click(i)).grid(row=(9-i)//3 + 4, column=(i-1)%3)
def button_clear_command() :
    entry1.delete(0,END)
def button_calculate() :
    try :
        answer=eval(var.get())
        var.set(answer)
    except ZeroDivisionError :
        var.set ("ERROR division by zero")
    except Exception :
        var.set(f"ERROR ") #si il y'a un erreur
    
def delete_button() :
    entry1.delete(entry1.index(INSERT)-1) 
def roll_back() :
    entry1.icursor(entry1.index(INSERT)-1)
def go_ahead() :
    entry1.icursor(entry1.index(INSERT)+1)
Button(window,text="=",width=8,height=4 ,command=button_calculate,background="red").grid(row=7,column=3)
Button(window,text="AC",width=8,height=4 ,command=button_clear_command,background="red").grid(row=3,column=0)
Button(window,text="+",width=8,height=4 ,command=lambda :button_click("+"),background="blue").grid(row=6,column=3)
Button(window,text="-",width=8,height=4 ,command=lambda : button_click("-"),background="blue").grid(row=5,column=3)
Button(window,text="*",width=8,height=4 ,command=lambda :button_click("*"),background="blue").grid(row=4,column=3)
Button(window,text="/",width=8,height=4 ,command=lambda :button_click("/"),background="blue").grid(row=3,column=3)
Button(window,text="%",width=8,height=4 ,command=lambda :button_click("%"),background="blue").grid(row=3,column=2)
Button(window,text="del",width=8,height=4 ,command=delete_button,background="red").grid(row=3,column=1)
Button(window,text="exp()",width=8,height=4 ,command=lambda :button_click("exp()"),background="blue").grid(row=2,column=0)
Button(window,text="ln()",width=8,height=4 ,command=lambda :button_click("ln()"),background="blue").grid(row=2,column=1)
Button(window,text="π",width=8,height=4,command=lambda :button_click("pi")).grid(row=7,column=1)
Button(window,text=".",width=8,height=4,command=lambda :button_click(".")).grid(row=7,column=2)
Button(window,text="√ ",width=8,height=4 ,command=lambda :button_click("sqrt()"),background="blue").grid(row=2,column=2)
Button(window,text="cos() ",width=8,height=4 ,command=lambda :button_click("cos()"),background="blue").grid(row=1,column=0)
Button(window,text="sin() ",width=8,height=4 ,command=lambda :button_click("sin()"),background="blue").grid(row=1,column=1)
Button(window,text="tan() ",width=8,height=4 ,command=lambda :button_click("tan()"),background="blue").grid(row=1,column=2)
Button(window,text="▲ ",width=8,height=4 ,command=go_ahead,background="blue").grid(row=1,column=3)
Button(window,text="▼ ",width=8,height=4 ,command=roll_back,background="blue").grid(row=2,column=3)
window.mainloop()