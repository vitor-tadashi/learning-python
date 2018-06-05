import turtle


def draw_square(drawer):
    drawer.shape("turtle")
    drawer.color("white")
    drawer.speed(10)

    for x in range(0, 4):
        drawer.forward(100)
        drawer.right(90)


def draw_circle(drawer):
    drawer.shape("turtle")
    drawer.color("purple")
    drawer.speed(2)
    drawer.circle(100)


def draw_triangle(drawer):
    drawer.shape("turtle")
    drawer.color("red")

    for x in range(0, 3):
        drawer.forward(100)
        drawer.left(120)


def draw_circule_with_square(drawer):
    drawer.shape("turtle")
    drawer.color("white")

    for x in range(0, 72):
        draw_square(drawer)
        drawer.right(5)


window = turtle.Screen()
window.bgcolor("black")
draw_circule_with_square(turtle.Turtle())
window.exitonclick()