def fat(n):
    if n == 0:
        return 1
    else:
        res = n * fat(n-1)  # n! = n * (n - 1)!
        return res


print(fat(4))
