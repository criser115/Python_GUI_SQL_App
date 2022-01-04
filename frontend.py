"""
A program that stores valve tagging information:
Tag, P&ID, Line-Equip, Station

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple

        index = list1.curselection()[0]
        selected_tuple = list1.get(index)

        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(tag_text.get(), pid_text.get(), line_equip_text.get(), station_text.get(),
                              valve_type_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(tag_text.get(), pid_text.get(), line_equip_text.get(), station_text.get(), valve_type_text.get())
    list1.delete(0, END)
    list1.insert(END, (tag_text.get(), pid_text.get(), line_equip_text.get(), station_text.get(),
                       valve_type_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])
    

def update_command():
    backend.update(selected_tuple[0], tag_text.get(), pid_text.get(), line_equip_text.get(), station_text.get(),
                   valve_type_text.get())


window = Tk()


window.wm_title("Valve Tag List")

# Label Section

l1 = Label(window, text="Tag")
l1.grid(row=0, column=0)

l2 = Label(window, text="P&ID")
l2.grid(row=0, column=2)

l3 = Label(window, text="Line-Equip")
l3.grid(row=1, column=0)

l4 = Label(window, text="Station")
l4.grid(row=1, column=2)

l5 = Label(window, text="Valve Type")
l5.grid(row=2, column=0)

# Text entry Section

tag_text = StringVar()
e1 = Entry(window, textvariable=tag_text)
e1.grid(row=0, column=1)

pid_text = StringVar()
e2 = Entry(window, textvariable=pid_text)
e2.grid(row=0, column=3)

line_equip_text = StringVar()
e3 = Entry(window, textvariable=line_equip_text)
e3.grid(row=1, column=1)

station_text = StringVar()
e4 = Entry(window, textvariable=station_text)
e4.grid(row=1, column=3)

valve_type_text = StringVar()
e5 = Entry(window, textvariable=valve_type_text)
e5.grid(row=2, column=1)

# List box & Scroll bar Section

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

list1.bind("<<ListboxSelect>>", get_selected_row)

# Button Section

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
