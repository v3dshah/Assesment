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
lblfirstname = ttk.Label(root, text="First Name: ", font=("Helvetica 20"))
lbllastname = ttk.Label(root, text="Last Name: ", font=("Helvetica 20"))


lbltitle.grid(row=0, column=1, columnspan=2)
lblfirstname.grid(row=1, column=0, columnspan=2)
lbllastname.grid(row=2, column=0, columnspan=2)

root.geometry("500x450")
root.mainloop()
