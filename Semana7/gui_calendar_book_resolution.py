from tkinter import Tk, Label
from calendar import monthrange

raiz = Tk()


def cal(year, month):
    days = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
    # cria e posiciona labels de dia da semana
    for i in range(7):
        label = Label(raiz, text=days[i])
        label.grid(row=0, column=i)

    """
    A iteração também é usada para criar e posicionar os labels com números.
    As variáveis week e weekday registram a linha e a coluna, respectivamente.
    """
    # Obtém o dia da semana para o primeiro dia do mês e
    # o número de dias no mês
    weekday, num_days = monthrange(year, month)
    # cria calendário iniciado na semana (linha) 1 e dia (coluna) 1
    week = 1
    for i in range(1, num_days + 1):  # para i = 1, 2, ..., numDays
        # cria label i e o coloca na linha week, coluna weekday
        label = Label(raiz, text=str(i))
        label.grid(row=week, column=weekday)
        # atualiza weekday(coluna) e week (linha)
        weekday += 1
        if weekday > 6:
            week += 1
            weekday = 0
    raiz.mainloop()


cal(2016, 7)
