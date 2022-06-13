#This program creates a GUI for Julies Party Hire
#Author: Ved
#Date: 10 June 2022

#Import tkinter
from tkinter import*
from tkinter import ttk

root=Tk()

#Create quit subroutine
def quit():
    main_window.destroy()


#Create labels
lbltitle = ttk.Label(root, text="Julies Party Hire", font=("Helvetica 30 bold"))

lbltitle.grid(row=0, column=0, columnspan=2)


root.geometry("500x450")
root.mainloop()
