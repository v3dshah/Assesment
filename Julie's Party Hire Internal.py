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




def check_inputs():
    # these are the global variables that are used
    global hire_details, entry_firstname, entry_lastname, entry_receiptnumber, entry_itemhired, entry_numberitemhired, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)
    Label(main_window, text="               ") .grid(column=2, row=4)
    Label(main_window, text="               ") .grid(column=2, row=5)
   #customer name 
    #cannot be blank
    if len(entry_firstname.get()) == 0:
        Label(main_window,fg='red',text="Required ",font='Helveitca 12').grid(column=2,row=1)
        entry_check=1

    if len(entry_lastname.get()) == 0:
        Label(main_window,fg='red',text="Required ",font='Helveitca 12').grid(column=2,row=2)
        entry_check=1

#receipt number
    #cannot be blank
    hasAlpha2 = False
    hasSpace2 = False
    for y in entry_receiptnumber.get():
        if y.isalpha():
            hasAlpha2 = True
        elif y.isspace():
            hasSpace2 = True
    #Ensure is digit
    if entry_receiptnumber.get().isdigit():
        Label(main_window, text="                  ").grid(column=2,row=3,sticky=W)
        Label(main_window, text="                  ").grid(column=2,row=3,sticky=W)
        entry_check = 0
    else:
        Label(main_window, fg='red', text="Enter a number",font='Helveitca 12').grid(column=2,row=3)
        entry_check = 1

#item hired ensure is not left blank
    if len(entry_itemhired.get()) == 0:
        Label(main_window,fg='red',text="Required ",font='Helveitca 12').grid(column=2,row=4)
        entry_check=1

#Number of item hired ensure number between 1-500
    if (entry_numberitemhired.get().isdigit()):
        if 0 < int(entry_numberitemhired.get()) <= 500:
            Label(main_window, text="                  ").grid(column=2,row=5)
            Label(main_window, text="                  ").grid(column=2,row=5)
            entry_check = 0
        else:
            Label(main_window, fg='red', text="Enter number between 1-500",font='Helveitca 12').grid(column=2,row=5)
            Label(main_window, fg='red', text="Enter number between 1-500",font='Helveitca 12').grid(column=2,row=5)
            entry_check = 1  
    else:
        Label(main_window, fg='red', text="Enter number between 1-500",font='Helveitca 12').grid(column=2,row=5)
        Label(main_window, fg='red', text="",font='Helveitca 12').grid(column=2,row=5)
        entry_check = 1

#if entrys all valid, append
    if entry_check == 0:
        append()








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
    Button(main_window, text="Append", font=("Helvetica 12"), width=10, command=check_inputs).grid(column=3,row=1)
    Button(main_window, text="Print", font=("Helvetica 12"), width=10, command=print_details).grid(column=4,row=1)
    Button(main_window, text="Quit", font=("Helvetica 12"), width=10, command=quit) .grid(column=5,row=1)
    Button(main_window, text="Delete", font=("Helvetica 12"), width=10,  command=delete_row).grid(column=3,row=4)

#Create Entry Boxes



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
delete_item .grid(column=4,row=5, sticky = W)


hire_details = []
total_entries = 0

main_window.geometry("1000x500")
main_window.title("Database of Julie's Party Hire")
buttons()
main_window.mainloop()
