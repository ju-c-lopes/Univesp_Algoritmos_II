def convert(num, base, dig=''):
    hexa = ['A', 'B', 'C', 'D', 'E', 'F']
    if num < base:
        if num >= 10:
            num = hexa[num - 10]
            dig = str(num) + dig
        else:
            dig = str(num) + dig
        # dig = str(num) + dig
    else:
        resto = num % base
        if resto >= 10:
            resto = hexa[resto - 10]
            dig = str(resto) + dig
        else:
            dig = str(resto) + dig
        conv = num // base
        return convert(conv, base, dig)
    return dig + f' base({base})'


print(convert(1453, 16))

"""
ACIMA: minha implementação antes de verificar a resolução
ABAIXO: a resolução da lição, muito mais simples
"""


def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        valor = convert_string[n]
        return convert_string[n]
    else:
        no = n % base
        valor = convert_string[no]
        return to_str(n//base, base) + convert_string[no]


print(to_str(1453, 16))
