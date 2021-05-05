print("Lista de Compras\n")
TotGeral = 0
adic = ""
for S in open("lista_compras.csv", "r", encoding="UTF-8"):
    S = S.rstrip()
    L = S.split(",")
    L[1], L[2] = int(L[1]), float(L[2])
    TotProd = L[1] * L[2]
    TotGeral += TotProd
    adic += " {0:>12}: {1:3} x{2:6.2f} = {3:7.2f}\n".format(L[0], L[1], L[2], TotProd)
    print(" {0:>12}: {1:3} x{2:6.2f} = {3:7.2f}"
          .format(L[0], L[1], L[2], TotProd))  # Cont. linha anterior

arq = open("ex_cvs.txt", "w", encoding="UTF-8")
adic += "-" * 38
adic += "\n"
adic += "Total da Lista de Compras {0:>10}".format(TotGeral)
arq.write(adic)
arq.close()
print("-" * 38)
print("Total da Lista de Compras {0:>10}".format(TotGeral))
