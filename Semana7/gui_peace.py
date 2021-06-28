import tkinter

raiz = tkinter.Tk()
text = tkinter.Label(raiz,
                     font=('Arial', 16, 'italic'),
                     text='Peace & Love',
                     foreground='white',
                     background='black',
                     padx=50,
                     pady=70)
text.pack(side=tkinter.LEFT)

img = tkinter.PhotoImage(file='peace.gif')
img_lab = tkinter.Label(raiz, image=img)
img_lab.pack(side=tkinter.RIGHT, expand=True, fill='both')
raiz.mainloop()
