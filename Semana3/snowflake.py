import turtle


def koch(num):
    if num == 0:
        return 'F'
    else:
        tmp = koch(num - 1)
        return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp


def draw_snowflake(n):
    s = turtle.Screen()
    t = turtle.Turtle()
    directions = koch(n)
    for i in range(3):
        for move in directions:
            if move == 'F':
                t.forward(300/3**n)
            if move == 'L':
                t.left(60)
            if move == 'R':
                t.right(120)
        t.right(120)
