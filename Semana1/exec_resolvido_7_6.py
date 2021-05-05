def grava_le(grava, le):
    print("\n--", grava, " para ", le, "-"*29)
    arq = open("arquivo.txt", "w", encoding=grava)
    arq.write(S)
    arq.close()
    arq = open("arquivo.txt", "r", encoding=le)
    l = arq.readlines()
    arq.close()
    for x in l:
        print(x)
    print("-"*50)


# A execução do programa começa por aqui
print("\nDemonstra os conflitos de codificação de arquivos\n\n")
S = """Uma boa porção de caracteres com acento
Maiúsculas: Á É Í Ó Ú Ã Õ Â Ê Ô À Ç
Minúsculas: á é í ó ú ã õ â ê ô à ç"""
while True:
    print("O que deseja fazer?")
    print(" para gravar ANSI e ler ANSI digite 1")
    print(" para gravar UTF8 e ler UTF8 digite 2")
    print(" para gravar ITF8 e ler ANSI digite 3")
    print(" para gravar ANSI e ler UTF8 digite 4")
    print("para sair digite 0")
    opc = int(input(" ...opc = "))
    if opc == 0:
        break
    elif opc == 1:
        grava_le("ANSI", "ANSI")
    elif opc == 2:
        grava_le("UTF-8", "UTF-8")
    elif opc == 3:
        grava_le("UTF-8", "ANSI")
    elif opc == 4:
        grava_le("ANSI", "UTF-8")


print("\nFim do Programa")
