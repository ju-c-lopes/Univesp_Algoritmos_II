def revert(s, s2='', i=0):
    lista = list(s)
    if len(lista) == 1:
        return s2 + lista[0]
    else:
        s2 = lista.pop(i) + s2
        i += 1
        return s2 + revert(s, s2, i)


print(revert('maravilha'))
# palavra = 'a h l i v a r a m'
# palavra.   8 7 6 5 4 3 2 1 0
