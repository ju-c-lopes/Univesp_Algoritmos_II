print("Inicio de Programa\n")

n = int(input("Digite um número para verificarmos se ele é primo: "))
print("\n")


def ver_primo(num):
    i = 1
    cont = 0
    while i <= num:
        if num % i == 0:
            cont += 1
        i += 1

    if cont > 2:
        return False
    else:
        return True


primos = ""

for numero in range(1, n):
    if ver_primo(numero):
        primos += f"{numero}\n"

arq = open("primos.txt", "w", encoding="UTF-8")
cab = f"Os números primos até {n} são:\n"
cab += f"{primos}"
arq.write(cab)
arq.close()

print("\nFim de Programa")
