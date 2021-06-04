def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


print(f'Função {list_sum([1, 3, 5, 7, 9])}')

soma_1 = ((((1 + 3) + 5) + 7) + 9)

print(f'Soma 1 "((((1 + 3) + 5) + 7) + 9)" = {soma_1}')

soma_2 = (1 + (3 + (5 + (7 + 9))))

print(f'Soma 2 "(1 + (3 + (5 + (7 + 9))))" = {soma_2}')

print("EXPLICAÇÃO:\n")
print("total = (1 + (3 + (5 + '_______'))) # resolve primeiro o laço mais interno\n"
      ".                       (7 + 9)\n"
      ".   total = (1 + (3 + '________')) # resolve próximo laço mais interno com a soma anterior\n"
      ".                      (5 + 16)\n"
      ".        total = (1 + '________') # resolve próximo laço mais interno com a soma anterior\n"
      ".                      (3 + 21)\n"
      ".                total = (1 + 24) # por fim, resolve a última soma, resultando o total final\n"
      ".\n"
      ".                      total = 25")


def soma_lista(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list + list_sum(num_list[1:])


print(f'\n{list_sum([1, 3, 5, 7, 9])}')

print("""
TESTE:

def soma(a, b=0):
    return a + b

print(soma(9, soma(7, soma(5, soma(3, soma(1))))))
""")


def soma(a, b=0):
    return a + b


print(soma(9, soma(7, soma(5, soma(3, soma(1))))))
