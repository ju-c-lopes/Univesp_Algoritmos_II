def cheers(n):
    if n == 0:
        print('Hurrah!!!', end='')
    else:
        print('Hip ', end='')
        cheers(n - 1)


cheers(4)