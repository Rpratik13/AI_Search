import turtle as ttl

box_length = 50  # Length of the rectangle
box_half_length = box_length / 2
box_height = 25  # Height of the rectangle
x_padding = 10  # Padding between rectangle
y_padding = 30  # Padding between depths
font = ("Arial", 12, "normal")
starting_y = 300  # Y position for the root rectangle


def initialize_turtle() -> None:
    """
    Initializes turtle for usage.

    Returns:
        None: This function does not return anything.
    """

    ttl.speed(0)

    ttl.up()
    ttl.goto(0, starting_y)
    ttl.down()


def create_box(name: str, is_goal=False, cost=None) -> None:
    """
    Creates a rectangle.

    Args:
        name (str): The text to be placed in the box.
        is_goal (bool): Creates a greed background if the box is a goal.
        cost (str): Cost from previous node to current node.

    Returns:
        None: This function does not return anything.
    """

    ttl.down()
    ttl.fillcolor("green" if is_goal else "white")

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
    ttl.write(name[:4], font=font)
    ttl.forward(box_half_length - 5)
    ttl.right(90)
    ttl.forward(0.2 * box_height)
    ttl.left(90)

    if cost is not None:
        ttl.left(180)
        ttl.forward(box_half_length)
        ttl.right(90)
        ttl.forward(25)
        ttl.write(cost, font=font)
        ttl.right(180)
        ttl.forward(25)
        ttl.left(90)
        ttl.forward(box_half_length)

    move_y(box_height)


def move(x: int, y: int) -> None:
    """
    Moves cursor to (x, y) coordinate.

    Args:
        x (int): X coordinate.
        y (int): Y coordinate.

    Returns:
        None: This function does not return anything.
    """

    ttl.up()
    ttl.goto(x, y)
    ttl.down()


def move_y(y: int) -> None:
    """
    Moves cursor to y distance in y-axis.

    Args:
        y (int): Y coordinate.

    Returns:
        None: This function does not return anything.
    """

    ttl.up()
    ttl.left(90)
    ttl.forward(y)
    ttl.right(90)
    ttl.down()


def done():
    """
    End the turtle session.

    Returns:
        None: This function does not return anything.
    """
    ttl.done()


def draw_line(x: int, y: int) -> None:
    """
    Draws line from current position to (x, y) coordinate.

    Args:
        x (int): X coordinate.
        y (int): Y coordinate.

    Returns:
        None: This function does not return anything.
    """

    current_position = ttl.pos()
    ttl.setpos(x, y)
    ttl.setpos(current_position[0], current_position[1])
