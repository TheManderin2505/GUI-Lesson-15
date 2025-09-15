from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("200x200")
root.title("File Management sys")

menubar = Menu(root)

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu = file)

file.add_command(label = 'New File',command = None)
file.add_command(label = 'Open...',command=None)
file.add_command(label='save',command=None)

file.add_separator()
file.add_command(label='Exit',command=root.destroy)

edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label = 'Edit',menu = edit)

edit.add_command(label = 'Cut',command = None)
edit.add_command(label = 'Copy', command = None)
edit.add_command(label='Paste',command = None)
edit.add_separator()
edit.add_command(label= 'Undo',command = None)
edit.add_command(label ='Redo',command = None)

help = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=help)

help.add_command(labe='Report Isue',command = None)
help.add_command(label='Walkthrough',command = None)
help.add_separator()
help.add_command(label='About Tk',command = None)

root.config(menu=menubar)
root.mainloop()