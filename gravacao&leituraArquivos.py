print("Inicio de Programa")

# Parte 1 - Gravação do arquivo

G = "Gravação e Leitura de Arquivo Texto"  # carrega o string G
arq = open("Exemplo7_1.txt", "w")          # abre o arquivo p/ gravar
arq.write(G)                               # executa a gravação
arq.close()                                # fecha o arquivo

# Parte 2 - Leitura do arquivo gravado na Parte 1

arq = open("Exemplo7_1.txt", "r")          # abre o arquivo para ler
L = arq.readline()                         # executa a leitura
arq.close()                                # fecha o arquivo
print("String lido - {}".format(L))        # exibe o string lido

print("Fim do Programa")
