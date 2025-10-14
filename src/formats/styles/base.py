from pydantic import BaseModel, Field


from .constants import Alignment
from ..borders.base import BorderStyle
from ..fonts.base import FontStyle
from ..colors.constants import Color


class TableStyle(BaseModel):
    name: str
    font: FontStyle
    border: BorderStyle | None = None
    alignment: Alignment = Alignment.LEFT
    fill_color: Color = Color.WHITE
