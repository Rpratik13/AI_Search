import turtle as ttl

box_length = 50
box_half_length = box_length / 2
box_height = 25
x_padding = 10
y_padding = 30
font = ("Arial", 12, "normal")
starting_y = 300

ttl.speed(0)

ttl.up()
ttl.goto(0, starting_y)
ttl.down()


def createBox(name, isGoal=False, cost=""):
    ttl.down()
    ttl.fillcolor("green" if isGoal else "white")

    ttl.begin_fill()
    ttl.forward(box_half_length)
    ttl.right(90)
    ttl.forward(box_height)
    ttl.right(90)
    ttl.forward(box_length)
    ttl.right(90)
    ttl.forward(box_height)
    ttl.right(90)
    ttl.forward(box_half_length)
    ttl.end_fill()

    ttl.up()
    ttl.right(90)
    ttl.forward(0.8 * box_height)
    ttl.right(90)
    ttl.forward(box_half_length - 5)
    ttl.right(180)
    ttl.write(name[:4], font=("Arial", 16, "normal"))
    ttl.forward(box_half_length - 5)
    ttl.right(90)
    ttl.forward(0.2 * box_height)
    ttl.left(90)

    if cost:
        ttl.left(180)
        ttl.forward(box_half_length)
        ttl.right(90)
        ttl.forward(25)
        ttl.write(cost, font=("Arial", 16, "normal"))
        ttl.right(180)
        ttl.forward(25)
        ttl.left(90)
        ttl.forward(box_half_length)

    moveY(box_height)


def move(x, y):
    ttl.up()
    ttl.goto(x, y)
    ttl.down()


def moveY(y):
    ttl.up()
    ttl.left(90)
    ttl.forward(y)
    ttl.right(90)
    ttl.down()


def moveX(x):
    ttl.up()
    ttl.forward(x)
    ttl.down()


def line(x, y):
    ttl.pos(x, y)


def done():
    ttl.done()


def drawLine(x, y):
    currentPosition = ttl.pos()
    ttl.setpos(x, y)
    ttl.setpos(currentPosition[0], currentPosition[1])
