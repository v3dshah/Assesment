#This program creates a GUI for Julies Party Hire
#Author: Ved
#Date: 10 June 2022

#Import tkinter
from re import A
from tkinter import*
from tkinter import ttk

main_window=Tk()

#Create quit subroutine
def quit():
    main_window.destroy()

#Create append subroutine
def append():
    global hire_details, entry, entry1, entryIH, entry_quantity
    # append each item to its own area of the list
    customer_details.append([entry.get(), entry1.get(), entryIH.get(), entry_quantity.get()])
    #clear the boxes
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entryIH.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    total_entries += 1

#Create and grid labels
lbltitle = ttk.Label(main_window, text="Julies Party Hire", font=("Helvetica 20 bold"))
lblfirstname = ttk.Label(main_window, text="First Name: ", font=("Helvetica 15"))
lbllastname = ttk.Label(main_window, text="Last Name: ", font=("Helvetica 15"))
lblreceiptnumber = ttk.Label(main_window, text="Receipt Number: ", font=("Helvetica 15"))
lblitemhired = ttk.Label(main_window, text="Items Hired: ", font=("Helveitca 15"))

lbltitle.grid(row=0, column=1, columnspan=1)
lblfirstname.grid(row=1, column=0, columnspan=1, sticky = W)
lbllastname.grid(row=2, column=0, columnspan=1, sticky = W)
lblreceiptnumber.grid(row=3, column=0, columnspan=1, sticky = W)
lblitemhired.grid(row=4, column=0, columnspan=1, sticky = W)

#Create Buttons
def buttons():
    Button(main_window, text="Append", font=("Helvetica 12")).grid(column=4,row=1)
    Button(main_window, text="Print", font=("Helvetica 12")).grid(column=2,row=1)
    Button(main_window, text="Quit", font=("Helvetica 12"), command=quit) .grid(column=3,row=1)
    Button(main_window, text="Delete", font=("Helvetica 12")).grid(column=3,row=4)

#Create Entry Boxes

hire_details = []
entry_firstname = Entry(main_window, font="Helvitica 12")
entry_firstname.grid(column=1,row=1, sticky = W)

hire_details = []
entry_lastname = Entry(main_window, font="Helvitica 12")
entry_lastname.grid(column=1,row=2, sticky = W)

hire_details = []
entry_receiptnumber = Entry(main_window, font="Helvitica 12")
entry_receiptnumber.grid(column=1,row=3, sticky = W)

hire_details = []
entry_itemhired = Entry(main_window, font="Helvitica 12")
entry_itemhired.grid(column=1,row=4, sticky = W)



main_window.geometry("500x450")
buttons()
main_window.mainloop()
