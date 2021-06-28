from tkinter import Tk, Label, PhotoImage, LEFT, RIGHT
from time import strftime, localtime

root = Tk()
foto = PhotoImage(file="rocket.gif").subsample(5)
img = Label(master=root, image=foto)
img.pack(side=LEFT)
hora = strftime("Date: %d %b %Y\nTime: %H:%M %p", localtime())
agora = Label(master=root, text=hora)
agora.pack(side=RIGHT)
root.mainloop()
