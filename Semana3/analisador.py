import os

sign = {'Creeper': 'ye8009hgblublu',
        'Code Red': '99dh1blakvlack',
        'Blaster': 'fdp1-11-boso'}


def scan(pathname, signatures=sign):
    """
    varre recursivamente os arquivos contidos, direta ou indirretamente, na pasta pathname
    """
    for item in os.listdir(pathname):
        # para cada arquivo ou pasta na pasta pathname
        # cria path name para item chamado next
        # next = pathname + '/' + item      #  linux ou mac
        # next = pathname + '\' + item      #  windows
        prox = os.path.join(pathname, item)  # qualquer SO
        try:  # faz recursão cega sobre next
            scan(prox, signatures)
        except:
            # caso básico: exceção significa que prox é um arquivo
            # para cada assinatura de vírus
            for virus in signatures:
                # verifica se arquivo prox tem assinatura de virus
                if open(prox).read().find(signatures[virus]) >= 0:
                    print('{}, found virus {}'.format(prox, virus))
