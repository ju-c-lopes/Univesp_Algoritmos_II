from re import findall


def frequency(content):
    pattern = '[a-zA-Z0-9]+'            # Expressão regula para todos alfanuméricos
    words = findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary
