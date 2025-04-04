#import tkinter as tk
#from tkinter import *
#root =TK()
#import tkinter
#root=tkinter.Tk()
import tkinter as tk
import time


def update_time():
    label.config(text=time.strftime
                 ("%H:%M:%S\n%A , %B , %D,  %Y"))  #"\n%a, %b ,%d-%m-%y"
    label.after(1000,update_time)

root=tk.Tk()
root.title('Digital Clock')
#root.geometry('350x500')

label=tk.Label(root,font=("calibri",40,"bold"),bg='black',fg='white')
label.pack()

update_time()
root.mainloop()