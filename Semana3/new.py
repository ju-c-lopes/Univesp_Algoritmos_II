import turtle

s = turtle.Screen()
t = turtle.Turtle()


def paint(n):
    if n == 0:
        t.forward(50)
        print('F ', end='')
    else:
        paint(n - 1)
        t.left(60)
        print('L ', end='')
        t.forward(50)
        print('F ', end='')
        t.right(120)
        print('R ', end='')
        t.forward(50)
        print('F ', end='')
        t.left(60)
        print('L ', end='')
        paint(n - 1)
