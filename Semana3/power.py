def power(a, n):
    """Retorna 'a' à potência 'n'"""
    res = 1
    for i in range(n):
        res += a
    return res


cont = 0


def rpower(a, n):
    """Retorna 'a' à potência 'n'"""
    global cont
    if n == 0:                  # caso básico: n == 0
        return 1
    tmp = rpower(a, n//2)       # etapa recursiva: n > 0
    if n % 2 == 0:
        cont += 1
        return tmp * tmp        # a**n = a**(n//2) * a**a(n//2)
    else:
        cont += 2
        return a * tmp * tmp    # a**n = a**(n//2) * a**a(n//2) * a


def power2(n):
    return power(2, n)


def rpower2(n):
    return rpower(2, n)


def pow2(n):
    return 2**n
