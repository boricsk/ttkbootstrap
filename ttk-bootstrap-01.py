from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
#egy sima hello word app elkészitése

root = tb.Window(themename="superhero") # téma kiválasztása, bővebb info itt : https://ttkbootstrap.readthedocs.io/en/latest/themes/
#minden widget a téma szerint fog kinézni.
root.title('TTK Bootstrsp')
root.geometry('500x350')

count = 0
def Changer():
    global count
    count += 1
    if count % 2 == 0:
        my_Label.config(text="Hello World!") #A konfiggal lehet módosítani a widgeteket.
    else:
        my_Label.config(text="Goodbye World!")
        
#labels
'''
bootstyle ez alkalmazza a CSS ttk-ből jövő alapszin sémát,ezek:

Default, primary, secondary, success, info, warning, danger, light, dark
https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

Mivel importálva vannak a constansok, ezért csupa nagybetűvel is lehetne írni.
Az inverse egy hátteret készít a default szinének az ellentétjével.

'''
my_Label = tb.Label(text="Hello World!", font=("Helvetica",28),bootstyle="Default, inverse" )
my_Label.pack(pady=50)


#button
my_Button = tb.Button(text="Click me", bootstyle="primary, outline", command=Changer)
my_Button.pack(pady=50)
root.mainloop()