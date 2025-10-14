from .base import BorderStyle
from .constants import BorderSide
from ..colors.constants import Color

ALL_SIDES = [
    BorderSide.TOP,
    BorderSide.BOTTOM,
    BorderSide.LEFT,
    BorderSide.RIGHT,
]


ALL_BORDERS_BLACK = BorderStyle(color=Color.BLACK, sides=ALL_SIDES)
ALL_BORDERS_WHITE = BorderStyle(color=Color.WHITE, sides=ALL_SIDES)
