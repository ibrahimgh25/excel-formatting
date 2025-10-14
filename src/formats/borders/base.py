from pydantic import BaseModel

from .constants import BorderSide
from ..colors.constants import Color


class BorderStyle(BaseModel):
    color: Color = Color.BLACK
    thickness: int = 1
    sides: list[BorderSide] = [
        BorderSide.TOP,
        BorderSide.BOTTOM,
        BorderSide.LEFT,
        BorderSide.RIGHT,
    ]
    dashed: bool = False
