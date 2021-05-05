print("Inicio do programa\n")
Soma = 0
Cont = 0
arq = open("Inteiros.txt", "r")
S = arq.readline()                                   # garante que o laço seja iniciado
while S != "":
    N = int(S)                                       # converte o texto S para N
    Soma = Soma + N                                  # totaliza o valor N em Soma
    Cont = Cont + 1                                  # conta mais um elemento
    print("Elemento {0} = {1}".format(Cont, N))
    S = arq.readline()                               # lê a próxima linha

arq.close()
print("\nSoma = {0}".format(Soma))
print("\nFim do Programa")
