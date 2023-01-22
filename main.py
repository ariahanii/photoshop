from tkinter import *
root = Tk(screenName="photoshop")
from functions import *

toIconBtn = Button(master=root, command=ToIco, text="Convert to .ico")
toIconBtn.pack()



mainloop()