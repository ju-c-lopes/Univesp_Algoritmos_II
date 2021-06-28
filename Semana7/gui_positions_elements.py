from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file="madruga.gif").subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Arial", 18), text="Bem-vindo Amigos Python!")
text.pack(side=BOTTOM)
root.mainloop()
