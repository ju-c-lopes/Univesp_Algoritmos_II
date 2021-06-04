def hanoi(n, peg1, peg2, peg3):
    """move n discos de peg1 para peg3 usando peg2"""

    # caso básico: n == 0. Não faz nada

    if n > 0:               # etapa recursiva
        hanoi(n - 1, peg1, peg3, peg2)          # move n-1 discos do topo de peg1 para peg2
        move_disk(peg1, peg3)                   # move maior disco de peg1 para peg2
        hanoi(n - 1, peg2, peg1, peg3)          # move n-1 discos de peg2 para peg3


def move_disk(from_peg, to_peg):
    """Move disco do topo da from_peg para a to_peg"""
    disk = from_peg.pop_disk()
    to_peg.push(disk)
