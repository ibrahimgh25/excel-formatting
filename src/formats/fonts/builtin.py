from .base import FontStyle
from .constants import FontWeight
from ..colors.constants import Color


CALIBRI_NORMAL = FontStyle(name="Calibri", size=11, color=Color.BLACK)
CALIBRI_HEADER_WHITE = FontStyle(
    name="Calibri", weight=[FontWeight.BOLD], size=11, color=Color.WHITE
)
CALIBRI_HYPERLINK_BLUE = FontStyle(
    name="Calibri", weight=[FontWeight.UNDERLINE], size=11, color=Color.BLUE
)
