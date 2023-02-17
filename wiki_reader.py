
import wikipedia

from tkinter import *


def wiki(text):

    t = wikipedia.summary(text)

    Fact = t
    root = Tk()
    root.geometry("600x600")
    T = Text(root, height = 30, width = 30)

    l = Label(root, text = "result of the query")
    l.config(font =("Courier", 14))

    b2 = Button(root, text = "Exit", command = root.destroy)

    l.pack()
    T.pack()

    b2.pack()

    T.insert(END, Fact)

    mainloop()

