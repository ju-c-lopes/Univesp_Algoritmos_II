import time
# Sequência Fibonacci, versão recursiva


def fib_rec(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib_rec(num-1) + fib_rec(num-2)


# Sequencia Fibonacci, versão iterativa

def fib_it(num):
    res = num
    a, b = 0, 1
    for k in range(2, num+1):
        res = a + b
        a, b = b, res
    return res


# n = 35
# start = time.time()
# print(fib_rec(n))
# print('Recursive: {} seconds'.format(time.time() - start))
# start = time.time()
# print(fib_it(n))
# print('Iterative: {} seconds'.format(time.time() - start))
