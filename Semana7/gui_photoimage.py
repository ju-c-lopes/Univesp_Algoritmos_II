from tkinter import Tk, Label, PhotoImage

root = Tk()
photo = PhotoImage(file="madruga.gif").subsample(5)

hello = Label(master=root, image=photo, width=300, height=300)
hello.pack()
root.mainloop()
