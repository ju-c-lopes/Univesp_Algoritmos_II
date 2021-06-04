# Quando uma função chama a si mesma, é chamada de função recursiva
# Se a função for simples, podendo fugir de recursão, usa-se a função simples

def imprime_rec(lista, i=0):
    if i < len(lista):
        print(lista[i])
        imprime_rec(lista, i + 1)


imprime_rec([1, 3, 5, 7])
