from tkinter import *
from tkinter import ttk
import backend

def get_selected_row(event):
	try:
		global selected_tuple
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
	except IndexError:
		pass
	

def view_command():
	list1.delete(0,END)
	for row in sorted(backend.view()):
		list1.insert(END, row)

def search_command():
	list1.delete(0,END)
	for row in backend.search(item_name_text.get(),lot_number_text.get(),
	exp_date_text.get()):
		list1.insert(END, row)

def add_command():
	backend.insert(item_name_text.get(),lot_number_text.get(),
	exp_date_text.get())
	list1.delete(0,END)
	list1.insert(END,(item_name_text.get(),lot_number_text.get(),
	exp_date_text.get()))

def delete_command():
	backend.delete(selected_tuple[0])
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END, row)


def update_command():
	backend.update(selected_tuple[0],item_name_text.get(),lot_number_text.get(),
	exp_date_text.get())
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END, row)

def exp_check_command():
	list1.delete(0,END)
	for row in backend.expire(
	exp_date_text.get()):
		list1.insert(END, row)
	

window= Tk()

window.wm_title("Lab Supplies Expiration Manager")


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)


window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)

# Create Labels
l1 = Label(window,text='Item Name')
l1.grid(row=0,column=0, padx=4, sticky='nsew')

l2 = Label(window,text='Lot Number')
l2.grid(row=0,column=2, padx=4, sticky='nsew')

l3 = Label(window,text='Exp Date (YYYY/MM/DD)')
l3.grid(row=1,column=0, padx=4, sticky='nsew')

# Create Entry Boxes
item_name_text = StringVar()
e1 = Entry(window,textvariable=item_name_text)
e1.grid(row=0, column=1,padx=4, sticky='nsew')

lot_number_text = StringVar()
e2 = Entry(window,textvariable=lot_number_text)
e2.grid(row=0, column=3, padx=4, sticky='nsew')

exp_date_text = StringVar()
e3 = Entry(window,textvariable=exp_date_text)
e3.grid(row=1, column=1, padx=4, sticky='nsew')

# Create Listbox
list1=Listbox(window, height=6, width=35,)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, padx=10, sticky='nsew')

# Create Vertical Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, )

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Create Horizontal Scrollbar
sb2=Scrollbar(window, orient='horizontal')
sb2.grid(row=6, column=2, rowspan=4, )

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row )


# Create Buttons
b1=Button(window, text='View all', width=12, command=view_command)
b1.grid(row=2, column=3, pady=(5), sticky='nsew')

b2=Button(window, text='Search entry', width=12, command=search_command)
b2.grid(row=3, column=3, pady=(0,5), sticky='nsew')

b3=Button(window, text='Add entry', width=12, command=add_command)
b3.grid(row=4, column=3, pady=(0,5), sticky='nsew')

b4=Button(window, text='Update selected', width=12, command=update_command)
b4.grid(row=5, column=3, pady=(0,5), sticky='nsew')

b5=Button(window, text='Delete selected', width=12, command=delete_command)
b5.grid(row=6, column=3, pady=(0,5), sticky='nsew')

b6=Button(window, text='Exp Check', width=12, command=exp_check_command)
b6.grid(row=7, column=3, pady=(0,5), sticky='nsew')

b7=Button(window, text='Close', width=12, command=window.destroy)
b7.grid(row=8, column=3, pady=(0,5), sticky='nsew')

window.mainloop()
