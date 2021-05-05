from random import randint

numeros = [randint(1, 5000) for i in range(1, 50)]

arq = open("numeros.txt", 'w', encoding="UTF-8")
text = ""
for i in numeros:
    text += f"{i}\n"

arq.write(text)
arq.close()

print("Executado com sucesso\n\nFim de Programa")
