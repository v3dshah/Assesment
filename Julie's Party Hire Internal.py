#This program creates a GUI for Julies Party Hire
#Author: Ved
#Date: 10 June 2022

#Import tkinter
from tkinter import*
from tkinter import ttk

main_window=Tk()

#Create quit subroutine
def quit():
    main_window.destroy()


#Create and grid labels
lbltitle = ttk.Label(main_window, text="Julies Party Hire", font=("Helvetica 30 bold"))
lblfirstname = ttk.Label(main_window, text="First Name: ", font=("Helvetica 20"))
lbllastname = ttk.Label(main_window, text="Last Name: ", font=("Helvetica 20"))
lblreceiptnumber = ttk.Label(main_window, text="Receipt Number: ", font=("Helvetica 20"))
lblitemhired = ttk.Label(main_window, text="Items Hired: ", font=("Helvetica 20"))

lbltitle.grid(row=0, column=1, columnspan=1)
lblfirstname.grid(row=1, column=0, columnspan=1, sticky = W)
lbllastname.grid(row=2, column=0, columnspan=1, sticky = W)
lblreceiptnumber.grid(row=3, column=0, columnspan=1, sticky = W)
lblitemhired.grid(row=4, column=0, columnspan=1, sticky = W)

#buttons
def buttons():
    Button(main_window, text="Update").grid(column=5,row=1)
    Button(main_window, text="Print").grid(column=2,row=1)
    Button(main_window, text="Quit",command=quit) .grid(column=3,row=1)
    Button(main_window, text="Delete").grid(column=4,row=6)




lbltitle.grid(row=0, column=1, columnspan=1)
lblfirstname.grid(row=1, column=0, columnspan=1, sticky = W)
lbllastname.grid(row=2, column=0, columnspan=1, sticky = W)
lblreceiptnumber.grid(row=3, column=0, columnspan=1, sticky = W)
lblitemhired.grid(row=4, column=0, columnspan=1, sticky = W)


main_window.geometry("500x450")
buttons()
main_window.mainloop()
