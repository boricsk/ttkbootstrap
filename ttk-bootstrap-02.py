from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
#checkbuttons, toolbuttons, togglebuttons 

root = tb.Window(themename="superhero") 
root.title('TTK Bootstrsp')
root.geometry('500x350')

count = 0
def Checker():
    if var1.get() == 1:
        my_label.config(text="Checked")
    else:
        my_label.config(text="Unchecked")
        
        
#Label
my_label = tb.Label(text="Click the checkbutton below!", font=("Helvetica", 18))
my_label.pack(pady=(40,10)) #40 felülről és 10 az alatta lévőtől

#checkbttn
'''
onvalue az az érték amikor ki van pipálva, az offvalue amikor nincs.

'''
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", 
                          text="Check me out!",
                          variable=var1, 
                          onvalue=1, 
                          offvalue=0, 
                          command=Checker)
my_check.pack(pady=10)

#toolbutton
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton",
                           text="Tool button",
                           variable=var2, 
                           onvalue=1, 
                           offvalue=0, 
                           command=Checker)
my_check2.pack(pady=10)

#outlinetoolbutton
var3 = IntVar()
my_check3 = tb.Checkbutton(bootstyle="danger, toolbutton, outline",
                           text="Outline Tool button",
                           variable=var3, 
                           onvalue=1, 
                           offvalue=0, 
                           command=Checker)
my_check3.pack(pady=10)

#round toggle button
var4 = IntVar()
my_check4 = tb.Checkbutton(bootstyle="success, round-toggle",
                           text="Round toggle button",
                           variable=var4, 
                           onvalue=1, 
                           offvalue=0, 
                           command=Checker)
my_check4.pack(pady=10)

#Square toggle button
var5 = IntVar()
my_check5 = tb.Checkbutton(bootstyle="warning, square-toggle",
                           text="Round toggle button",
                           variable=var5, 
                           onvalue=1, 
                           offvalue=0, 
                           command=Checker)
my_check5.pack(pady=10)

root.mainloop()