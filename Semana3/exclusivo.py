def dup1(lst):
    """
    Retorna True se lista lst tiver duplicatas; caso contrário, False
    """
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False


def dup2(lst):
    """
    Retorna True se lista lst tiver duplicatas; caso contrário, False
    """
    lst.sort()
    for index in range(1, len(lst)):
        if lst[index] == lst[index - 1]:
            return True
    return False


def dup3(lst):
    """
    Retorna True se lista lst tiver duplicatas, caso contrário, False
    """
    s = set()
    for item in lst:
        if item in s:
            return False
        else:
            s.add(item)
    return True


def dup4(lst):
    """
    Retorna True se lista lst tiver duplicatas, caso contrário, False
    """
    return len(lst) != len(set(lst))
