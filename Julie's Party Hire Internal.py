#This program creates a GUI for Julies Party Hire


#Import tkinter
from tkinter import*
from tkinter import ttk

main_window=Tk()

#Create quit subroutine
def quit():
    main_window.destroy()

#Print customer details
def print_details():
    # these are the global variables that are used
    global  total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="First Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Last Name").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Receipt Number").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Items Hired").grid(column=4, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of Items Hired").grid(column=5, row=7)
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][2])).grid(column=3, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][3])).grid(column=4, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][4])).grid(column=5, row=name_count+8)
        name_count += 1 
        print(name_count)




#Create append subroutine
def append():
    global hire_details, entry_firstname, entry_lastname, entry_receiptnumber, entry_itemhired, entry_numberitemhired, total_entries
    # append each item to its own area of the list
    hire_details.append([entry_firstname.get(), entry_lastname.get(), entry_receiptnumber.get(), entry_itemhired.get(), entry_numberitemhired.get()])
    #clear the boxes
    entry_firstname.delete(0, 'end')
    entry_lastname.delete(0, 'end')
    entry_receiptnumber.delete(0, 'end')
    entry_itemhired.delete(0, 'end')
    entry_numberitemhired.delete(0, 'end')
    total_entries += 1


def delete_row():
    # these are the global variables that are used
    global hire_details, delete_item, total_entries, name_count
    # find which row is to be deleted and delete it
    del hire_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7)
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    Label(main_window, text="       ").grid(column=5, row=name_count+7)
    # print all the items in the list
    print_details()

#Create and grid labels
lbltitle = ttk.Label(main_window, text="Julies Party Hire", font=("Helvetica 20 bold"))
lblfirstname = ttk.Label(main_window, text="First Name: ", font=("Helvetica 15"))
lbllastname = ttk.Label(main_window, text="Last Name: ", font=("Helvetica 15"))
lblreceiptnumber = ttk.Label(main_window, text="Receipt Number: ", font=("Helvetica 15"))
lblitemhired = ttk.Label(main_window, text="Items Hired: ", font=("Helveitca 15"))
lblnumberitemhired = ttk.Label(main_window, text="Number of Item Hired: ", font=("Helveitca 15"))
lbldeleterow = ttk.Label(main_window, text="Row #: ", font=("Helveitca 15"))

lbltitle.grid(row=0, column=1, columnspan=1)
lblfirstname.grid(row=1, column=0, columnspan=1, sticky = W)
lbllastname.grid(row=2, column=0, columnspan=1, sticky = W)
lblreceiptnumber.grid(row=3, column=0, columnspan=1, sticky = W)
lblitemhired.grid(row=4, column=0, columnspan=1, sticky = W)
lblnumberitemhired.grid(row=5, column=0, columnspan=1, sticky = W)
lbldeleterow.grid(row=5, column=3, columnspan=1, sticky = W)

#Create Buttons
def buttons():
    Button(main_window, text="Append", font=("Helvetica 12"), command=append).grid(column=4,row=1)
    Button(main_window, text="Print", font=("Helvetica 12"), command=print_details).grid(column=2,row=1)
    Button(main_window, text="Quit", font=("Helvetica 12"), command=quit) .grid(column=3,row=1)
    Button(main_window, text="Delete", font=("Helvetica 12"), command=delete_row).grid(column=3,row=4)

#Create Entry Boxes

hire_details = []
total_entries = 0

entry_firstname = Entry(main_window, font="Helvitica 12")
entry_firstname.grid(column=1,row=1, sticky = W)


entry_lastname = Entry(main_window, font="Helvitica 12")
entry_lastname.grid(column=1,row=2, sticky = W)


entry_receiptnumber = Entry(main_window, font="Helvitica 12")
entry_receiptnumber.grid(column=1,row=3, sticky = W)


entry_itemhired = Entry(main_window, font="Helvitica 12")
entry_itemhired.grid(column=1,row=4, sticky = W)


entry_numberitemhired = Entry(main_window, font="Helvitica 12")
entry_numberitemhired.grid(column=1,row=5, sticky = W)

delete_item = Entry(main_window)
delete_item .grid(column=4,row=5)

main_window.geometry("800x500")
buttons()
main_window.mainloop()
