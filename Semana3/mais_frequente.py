def frequent(lst):
    """Retorna item que ocorre com mais frequência na lista lst não vazia"""
    lst.sort()          # primeiro classifica lista

    current_len = 1     # tamanho da sequência atual
    longest_len = 1     # tamanho da sequência mais longa
    most_freq = lst[0]  # item com sequência mais longa

    for i in range(1, len(lst)):
        # compara item atual com anterior
        if lst[i] == lst[i - 1]:    # se igual
            # sequência atual continua
            current_len += 1
        else:                       # se não igual
            # atualiza sequência mais longa, se necessário
            if current_len > longest_len:       # se sequencia que terminou for maior até aqui
                longest_len = current_len       # armazena seu tamanho e o item
                most_freq = lst[i - 1]
            # inicia nova sequência
            current_len = 1
    return most_freq
