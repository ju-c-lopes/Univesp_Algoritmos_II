print("Inicio do programa\n")

L = []                                              # inicia a lista vazia
x = float(input("Digite um número real: "))
while x != 0:
    L.append("{:.3f}\n".format(x))                  # inclui o string em L
    x = float(input("Digite um número real: "))

arqreais = open("ValsReais2.txt", "w")              # abre o arquivo
arqreais.writelines(L)                              # grava a lista toda
arqreais.close()                                    # fecha o arquivo

print("\nFim do Programa")
