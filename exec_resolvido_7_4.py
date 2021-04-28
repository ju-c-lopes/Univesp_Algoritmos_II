from random import randint
print("Inicio do Programa\n")
N = 0
while N < 10 or N > 10000:            # leitura de N
    N = int(input("Digite N entre [10, 10000]: "))
cod = []
cont = 0
while cont < N:                       # laço para gerar a lista de códigos únicos
    a = randint(10000, 50000)
    if a not in cod:                  # este if garante a unicidade
        cod.append(a)
        cont += 1                     # só conta 1 quando entrou L


S = "{0};{1};{2:.2f};{3}\n"           # string pré formatado
ICMS = (7, 12, 18)                    # tupla com os 3 valores de ICMS
arq = open("Estoque.csv", "w")
cont = 0

while cont < N:
    Qtde = randint(1, 3800)
    PcUn = randint(180, 43590) / 100
    i = randint(0, 2)
    arq.write(S.format(cod[cont], Qtde, PcUn, ICMS[i]))
    cont += 1

arq.close()
print("\nFim do Programa")
