import time

m = dict()


def fib_rec(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib_rec(num-1) + fib_rec(num-2)


def fib_mem(num):
    if num < 2:
        return num
    elif m.get(num) is not None:
        return m[num]
    else:
        m[num] = fib_mem(num-1) + fib_mem(num-2)
        return m[num]


n = 25
start = time.time()
print(fib_rec(n))
print('Recursive: {} seconds'.format(time.time() - start))
start = time.time()
print(fib_mem(n))
print('Iterative: {} seconds'.format(time.time() - start))
