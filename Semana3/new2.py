import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(-300, -200)
t.pendown()


def paint(n):
    if n == 0:
        t.forward(1)
        print('F ', end='')
    else:
        paint(n - 1)
        t.left(60)
        print('L ', end='')
        paint(n - 1)
        # print('F ', end='')
        t.right(120)
        print('R ', end='')
        paint(n - 1)
        # print('F ', end='')
        t.left(60)
        print('L ', end='')
        paint(n - 1)
