from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE

raiz = Tk()
texto = Label(raiz,
              font=('Arial', 16, 'bold italic'),
              foreground='white',
              background='black',
              padx=25,
              pady=10,
              text='Vamos trabalhar com GUI!')
texto.pack(side=BOTTOM, expand=True, fill='both')
crowl = PhotoImage(file='madruga.gif').subsample(7)
crowl_label = Label(raiz,
                    borderwidth=3,
                    relief=RIDGE,  # estilo de borda do label
                    image=crowl,
                    height=250,
                    background='black')
crowl_label.pack(side=LEFT, expand=True, fill='both')
rocket = PhotoImage(file='rocket.gif').subsample(3)
rocket_label = Label(raiz,
                     image=rocket,
                     height=250,
                     background='black')
rocket_label.pack(side=RIGHT, expand=True, fill='both')
raiz.mainloop()

