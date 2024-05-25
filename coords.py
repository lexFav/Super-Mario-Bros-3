def reg(coordinates, grid):
    """pygame to regular coordinates"""

    x, y = coordinates
    x_axis, y_axis = grid

    x -= x_axis / 2
    if y > y_axis / 2:
        y = -y + (y_axis / 2)
    elif y < y_axis / 2:
        y = (y_axis / 2) - y
    else:
        y = 0

    return (x, y)

def pygame(coordinates, grid):
    """regular to pygame coordinates"""

    x, y = coordinates
    x_axis, y_axis = grid

    x += x_axis/2
    if y < 0:
        y = (y_axis / 2) - y
    elif y > 0:
        y = (y_axis / 2) - y
    else:
        y = y_axis / 2

    return (x, y)

if __name__ == "__main__":
    print(pygame([0, 0], [100, 100]))