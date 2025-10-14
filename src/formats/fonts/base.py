from pydantic import BaseModel

from .constants import FontWeight
from ..colors.constants import Color


class FontStyle(BaseModel):
    name: str
    weight: list[FontWeight] | None = None
    size: int = 11
    color: Color = Color.BLACK
