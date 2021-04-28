def bubble_sort(lista):
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - 1):
            if lista[j] > lista[j + 1]:
                troca = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = troca
    return lista


arq = open("numeros.txt", "r")
num_str = arq.read()
arq.close()
num_str = num_str.split("\n")
if num_str[-1] == "":
    num_str.pop()
for i in range(0, len(num_str)):
    num_str[i] = int(num_str[i])

num_str = bubble_sort(num_str)
lista_ord = ""
for i in range(0, len(num_str) - 1):
    lista_ord += str(num_str[i]) + "\n"

file = open("ordenados.txt", "w")
lista_ord = "Exercicio Ordenados com Bubble Sort\n" + ("="*40) + "\n" + lista_ord
file.write(lista_ord)
file.close()
