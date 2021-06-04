def kthsmallest(lst, k):
    """Retorna o k-ésimo menor item em lst"""
    lst.sort()
    return lst[k-1]
