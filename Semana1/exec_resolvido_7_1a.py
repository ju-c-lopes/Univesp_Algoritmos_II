print("Inicio do Programa")
arqreais = open("ValsReais.txt", "w")             # linha 2
x = float(input("Digite um número real: "))
while x != 0:
    arqreais.write("{0:.3f}\n".format(x))         # linha 5
    x = float(input("Digite um número real: "))
arqreais.close()                                  # linha 7
print("Fim do Programa")