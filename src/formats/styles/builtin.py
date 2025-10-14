from .base import TableStyle
from .constants import Alignment
from ..colors.constants import Color
from ..fonts.builtin import CALIBRI_NORMAL, CALIBRI_HEADER_WHITE, CALIBRI_HYPERLINK_BLUE
from ..borders.builtin import ALL_BORDERS_BLACK, ALL_BORDERS_WHITE
from ..borders.base import BorderStyle
from ..borders.constants import BorderSide

BLUE_HEADER_CENTERED = TableStyle(
    name="BlueHeaderCentered",
    font=CALIBRI_HEADER_WHITE,
    border=ALL_BORDERS_WHITE,
    alignment=Alignment.CENTER,
    fill_color=Color.DARK_BLUE,
)

BODY_CENTERED = TableStyle(
    name="BodyCentered",
    font=CALIBRI_NORMAL,
    border=ALL_BORDERS_BLACK,
    alignment=Alignment.CENTER,
    fill_color=Color.WHITE,
)

BODY_LEFT = TableStyle(
    name="BodyLeft",
    font=CALIBRI_NORMAL,
    border=ALL_BORDERS_BLACK,
    alignment=Alignment.LEFT,
    fill_color=Color.WHITE,
)

CUSTOM_HYPERLINK = TableStyle(
    name="CustomHyperlink",
    font=CALIBRI_HYPERLINK_BLUE,
    border=ALL_BORDERS_BLACK,
    alignment=Alignment.CENTER,
    fill_color=Color.WHITE,
)

_STYLE_REGISTRY = {
    "BlueHeaderCentered": BLUE_HEADER_CENTERED,
    "BodyCentered": BODY_CENTERED,
    "BodyLeft": BODY_LEFT,
    "CustomHyperlink": CUSTOM_HYPERLINK,
}


def get_style(style_name: str) -> TableStyle | str:
    style = _STYLE_REGISTRY.get(style_name, None)
    if style is None:
        raise ValueError(
            f"Style '{style_name}' is not defined. Available styles: {get_all_style_names()}"
        )
    return _STYLE_REGISTRY.get(style_name, style_name)


def get_all_style_names() -> list[str]:
    return list(_STYLE_REGISTRY.keys())
