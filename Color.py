from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4
    YELLOW = 5
    BLACK = 6
    ORANGE = 7

def get_rgb_value(color):
    """
    Get the rgb color from a enum
    :param color: Color object
    :returns tuple: 3 index tuple representing int values from 0-255
    """
    if color == Color.RED:
        return (255, 0 , 0)
    if color == Color.GREEN:
        return (0, 255, 0)
    if color == Color.BLUE:
        return (0, 0, 255)
    if color == Color.PURPLE:
        return (138,43,226)
    if color == Color.YELLOW:
        return (255,255,0)
    if color == Color.BLACK:
        return (0, 0, 0)
    if color == Color.ORANGE:
        return (255,165,0)