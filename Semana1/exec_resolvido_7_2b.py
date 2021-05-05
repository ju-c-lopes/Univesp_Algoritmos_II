print("Inicio do Programa\n")
Soma = 0
Cont = 0
for S in open("Inteiros.txt"):      # note que "r" foi omitido, pois é default
    N = int(S)
    Soma += N
    Cont = Cont + 1
    print("Elemento {0} = {1}".format(Cont, N))

print("\nSoma = {0}".format(Soma))
print("\nFim do Programa")
