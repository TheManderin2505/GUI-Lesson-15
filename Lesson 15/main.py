from tkinter import *
from gtts import gTTS
from  tkinter.ttk import *

root = Tk()
root.geometry("800x800")
root.title("Language learning app")

def dropdown_menu_commands_1():
    menu_val = dropdown_menu.get()

    if menu_val == "Quit?":
        quit()

#



dropdown_menu = Menu(root)
help = Menu(dropdown_menu,tearoff=0)
language = Menu(dropdown_menu,tearoff=0)
reportbug = Menu(dropdown_menu,tearoff=0)
dropdown_menu.add_cascade(label = "Help",menu=help)
dropdown_menu.add_cascade(label="Chose Language",menu = language)
dropdown_menu.add_cascade(label="Report a Bug",menu=reportbug)

#

help.add_command(label="App Walk through?",command = 0)
help.add_command(label="How to use guide",command = 0)

language.add_command(label="English",command = 0)
language.add_command(label="German",command= 0)


root.config(menu=dropdown_menu)
root.mainloop()