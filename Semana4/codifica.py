def codifica(word=''):
    print('Char   Decimal   Hexa  Binário')
    for c in word:
        cod = ord(c)
        # exibe o caractere(c) e seu código
        #      char decimal  hexa   binário
        print(' {}    {:7}   {:4x}   {:7b}'.format(c, cod, cod, cod))
