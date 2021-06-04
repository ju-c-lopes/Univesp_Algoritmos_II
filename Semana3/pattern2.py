def pattern2(n):
    if n > 0:
        pattern2(n - 1)
        print(n * '*')
        pattern2(n - 1)


pattern2(3)
