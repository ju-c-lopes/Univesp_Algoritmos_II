import tkinter
from calendar import monthrange

raiz = tkinter.Tk()


def calendar(y, m):
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for index in range(len(weekdays)):
        week_lab = tkinter.Label(raiz,
                                 padx=5, pady=5,
                                 text=weekdays[index])
        week_lab.grid(row=1, column=index)
    day, days = monthrange(y, m)
    d = 1
    for i in range(len(weekdays)):
        if i == 0:
            for j in range(day, len(weekdays)):
                day_month = tkinter.Label(raiz,
                                          padx=5, pady=5,
                                          text=d)
                d += 1
                day_month.grid(row=(i + 2), column=j)
        else:
            for j in range(len(weekdays)):
                if d > days:
                    break
                day_month = tkinter.Label(raiz,
                                          padx=5, pady=5,
                                          text=d)
                d += 1
                day_month.grid(row=i+2, column=j)


calendar(2021, 6)
raiz.mainloop()

