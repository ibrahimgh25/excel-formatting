from enum import Enum


class Alignment(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"


class BorderStyle(str, Enum):
    THIN = "thin"
    THICK = "thick"
    MEDIUM = "medium"
    DASHED = "dashed"
    DOTTED = "dotted"
    DOUBLE = "double"
