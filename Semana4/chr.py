def char(x, y):
    for i in range(x, y + 1):
        # Imprimirá na tela o valor ASCII e a sua representação
        # de como nós enxergamos ou estamos acostumados
        print(f'{i} : {chr(i)}')


hello_world = 'Hello\u0020World!'
hello_world_grego = '\u0393\u03b5\u03b9\u03b1\u0020\u03c3\u03b1\u03c2' \
                    '\u0020\u03ba\u03cc\u03c3\u03bc\u03bf!'
hello_world_mandarim = '\u4e16\u754c\u60a8\u597d!'

print(f'{hello_world}\n'
      f'{hello_world_grego}\n'
      f'{hello_world_mandarim}')
