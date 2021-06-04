def pattern(n):
    if n == 0:
        print(n, end=' ')
    else:
        pattern(n-1)
        print(n, end=' ')
        pattern(n-1)


pattern(3)
