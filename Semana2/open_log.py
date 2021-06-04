import time


def open_log(nomearq, modo):
    """
    Abre arquivo nomearq em certo modo e retorna referência ao arquivo aberto;
    registra o acesso ao arquivo em log.txt
    """

    arq_entrada = open(nomearq, modo)

    # obtem a hora atual

    now = time.localtime()
    now_format = time.strftime('%A %b/%d/%Y %I:%M %p', now)

    # abre arquivo log.txt no modo de acréscimo e acrescenta log
    arq_saida = open('log.txt', 'a')
    log = '{}: Arquivo {} aberto.\n'  # formata string
    arq_saida.write(log.format(now_format, nomearq))  # ('Arquivo {} aberto.\n'.format(nomearq))
    arq_saida.close()
    return arq_entrada
