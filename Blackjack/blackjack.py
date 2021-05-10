from baralho import Baralho


def total(mao):
    """
    Retorna o valor da mão de blackjack
    """
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    resultado = 0
    ases = 0

    # Soma os valores das cartas na mão, também soma o número de ases
    for carta in mao:
        resultado += valores[carta[0]]
        if carta[0] == 'A':
            ases += 1

    # Enquanto valor da mão > 21 e existe um às na mão
    # com valor 11, converte seu valor para 1
    while resultado > 21 and ases > 0:
        resultado -= 10
        ases -= 1

    return resultado


def compara_maos(casa, jogador):
    """
    Compara mãos da casa (computador) e do jogador, e mostra resultado
    """

    # Calcula total da mão da casa e do jogador
    total_casa, total_jogador = total(casa), total(jogador)

    if total_casa > total_jogador:
        print('Você perdeu.')
    elif total_casa < total_jogador:
        print('Você venceu!')
    elif total_casa == 21 and 2 == len(casa) < len(jogador):
        print('Você perdeu.')  # casa vence com um blackjack
    elif total_jogador == 21 and 2 == len(jogador) < len(casa):
        print('VocÇe venceu!')  # jogador vence com um blackjack
    else:
        print('Empatou')


def blackjack():
    """
    Simula a casa em um jogo blackjack
    """

    baralho = Baralho()
    baralho.embaralhar()  # apanha baralho misturado

    casa = []  # mão da casa
    jogador = []  # mão do jogador

    for i in range(2):              # distribui mão inicial em 2 rodadas
        baralho.distribui_carta(jogador)  # distribui para jogador primeiro
        baralho.distribui_carta(casa)  # distribui para casa depois

    # apresenta as mãos
    print('Casa: {:>7}{:>7}\n'.format(casa[0], casa[1]))
    print('Você: {:>7}{:>7}'.format(jogador[0], jogador[1]))

    # Enquanto usuário pede mais uma carta, a casa a entrega
    resposta = input("Deseja carta (c) - o default - ou parar (p)? ")
    while resposta in {'', 'c', 'carta'}:
        carta = baralho.distribui_carta(jogador)
        print('Você recebeu {:>7}'.format(carta))

        if total(jogador) > 21:  # Total do jogador é > 21
            print('Você ultrapassou... perdeu.')
            return

        resposta = input("Deseja carta (c) - o default - ou parar (p)? ")

    # A casa deve jogar pelas "regras da casa"

    while total(casa) < 17:
        carta = baralho.distribui_carta(casa)
        print('A casa recebeu {:>7}'.format(carta))

        if total(casa) > 21:  # Total da casa é > 21
            print('A casa ultrapassou... Você venceu!')
            return

    # compara as mãos da casa e do jogador e mostra resultado
    compara_maos(casa, jogador)
