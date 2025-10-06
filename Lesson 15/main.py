from tkinter import *
from gtts import gTTS
from  tkinter.ttk import *
import os


root = Tk()
root.geometry("800x600")
root.title("Language learning app")

def dropdown_menu_commands_1():
    menu_val = dropdown_menu.get()

    if menu_val == "Quit?":
        quit()


def translate():
    translate_from = entery_box_1.get()

une = False

def speak_aloud():#1
    audio1 = gTTS(text = entery_box_1.get(),lang = language,slow = une)
    audio1.save("audio.wav")
    os.system("audio.wav")

def speak_aloud_translated():#2
    g=2


#------

def change_lng_to_E():
    global language
    language = "en"
    label_1.config(text = "English")
def change_lng_2_G():
    global language
    language = "de"
    label_1.config(text = "German")

def change_lng_to_E2():
    global language1
    language1 = "en"
    label_2.config(text = "English")
def change_lng_2_G2():
    global language1
    language1 = "de"
    label_2.config(text = "German")

#-------



dropdown_menu = Menu(root)
help = Menu(dropdown_menu,tearoff=0)
language = Menu(dropdown_menu,tearoff=0)
reportbug = Menu(dropdown_menu,tearoff=0)
language2 = Menu(dropdown_menu,tearoff=0)
dropdown_menu.add_cascade(label = "Help",menu=help)
dropdown_menu.add_cascade(label="Chose Language to Translate from",menu = language)
dropdown_menu.add_cascade(label="Chose Language to Translate to",menu = language2)
dropdown_menu.add_cascade(label="Report a Bug",menu=reportbug)

#

help.add_command(label="App Walk through?",command = 0)
help.add_command(label="How to use guide",command = 0)

language.add_command(label="English",command = change_lng_to_E)
language.add_command(label="German",command= change_lng_2_G)

language2.add_command(label="English",command = change_lng_to_E2)
language2.add_command(label="German",command= change_lng_2_G2)
#

entery_box_1 = Entry(root,width = 35)
entery_box_1.place(x= 75,y = 175)

label_1 = Label(root,text = "Enter the Phrase you want to translate here",font = ("New Times Roman",10, 'bold'))
label_1.place(x=60,y=150)

entery_box_2 = Entry(root,width =30)
entery_box_2.place(x=500,y=175)

label_2 = Label(root, text = "Your Translated text is here",font = ("New Times Roman",10, 'bold'))
label_2.place(x=500,y=150)

button1 = Button(root, text = "Translate",command = translate)
button1.place(x=350,y= 350)

button2 = Button(root, text = "Speak Aloud",command = speak_aloud)
button2.place(x=60, y= 200)

button3 = Button(root, text = "Speak Aloud",command = speak_aloud_translated)
button3.place(x= 510,y=200)



root.config(menu=dropdown_menu)
root.mainloop()
