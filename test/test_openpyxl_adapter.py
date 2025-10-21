import pytest
from openpyxl.styles import NamedStyle, Border

from src.formats.styles.builtin import BLUE_HEADER_CENTERED
from src.formats.styles.base import TableStyle
from src.formats.fonts.base import FontStyle
from src.formats.borders.base import BorderStyle
from src.formats.colors.constants import Color
from src.formats.fonts.constants import FontWeight
from src.formats.borders.constants import BorderSide
from src.formats.styles.constants import Alignment as AlignmentEnum
from src.io.openpyxl_adapter import OpenPyXLStyleAdapter


@pytest.mark.parametrize(
    "weight,expected_weight",
    [
        ([FontWeight.BOLD], "B"),
        ([FontWeight.ITALIC], "I"),
        ([FontWeight.BOLD, FontWeight.ITALIC], "BI"),
        ([FontWeight.UNDERLINE], "U"),
        ([], ""),
        (None, ""),
    ],
)
def test_convert_font_weights(weight, expected_weight):
    style = get_fake_style(
        font=FontStyle(name="Arial", weight=weight, color=Color.BLACK)
    )
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.font.bold == ("B" in expected_weight)
    assert openpyxl_style.font.italic == ("I" in expected_weight)
    assert bool(openpyxl_style.font.underline) == ("U" in expected_weight)


def get_fake_style(name=None, font=None, border=None, alignment=None, fill_color=None):
    return TableStyle(
        name=name or "test",
        font=font or FontStyle(name="Arial", color=Color.BLACK),
        border=border,
        alignment=alignment or AlignmentEnum.LEFT,
        fill_color=fill_color or Color.WHITE,
    )


@pytest.mark.parametrize(
    "sides,expected_sides",
    [
        (
            [BorderSide.TOP, BorderSide.BOTTOM, BorderSide.LEFT, BorderSide.RIGHT],
            ["left", "right", "top", "bottom"],
        ),
        ([BorderSide.TOP], ["top"]),
        ([BorderSide.BOTTOM], ["bottom"]),
        ([BorderSide.LEFT], ["left"]),
        ([BorderSide.RIGHT], ["right"]),
        ([], []),
    ],
)
def test_convert_border_correctSides(sides, expected_sides):
    style = get_fake_style(
        border=BorderStyle(sides=sides, thickness=2, color=Color.BLACK)
    )
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert isinstance(openpyxl_style.border, Border)
    assert all(
        getattr(openpyxl_style.border, side) is not None for side in expected_sides
    )


@pytest.mark.parametrize(
    "thickness,expected_style",
    [
        (1, "thin"),
        (2, "medium"),
        (3, "thick"),
        (5, "thin"),  # Unknown thickness defaults to thin
    ],
)
def test_convert_border_matchingThickness(thickness, expected_style):
    style = get_fake_style(
        border=BorderStyle(
            sides=[BorderSide.TOP], thickness=thickness, color=Color.BLACK
        ),
    )
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.border.top.style == expected_style


def test_convert_border_matchingColor():
    style = get_fake_style(
        border=BorderStyle(sides=[BorderSide.TOP], thickness=1, color=Color.DARK_BLUE)
    )
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.border.top.color.rgb == "00002060"
    style = get_fake_style(
        border=BorderStyle(sides=[BorderSide.LEFT], thickness=1, color=Color.GREEN)
    )
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.border.left.color.rgb == "0000FF00"


def test_convert_defaultStyle_returnsValidOpenPyXLStyle():
    style = BLUE_HEADER_CENTERED
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)

    assert isinstance(openpyxl_style, NamedStyle)
    assert openpyxl_style.name == style.name


def test_convert_font_correctNameAndSize():
    style = get_fake_style(
        font=FontStyle(name="Times New Roman", size=14, color=Color.BLACK)
    )
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.font.name == "Times New Roman"
    assert openpyxl_style.font.size == 14


def test_convert_font_correctColor():
    style = get_fake_style(font=FontStyle(name="Arial", color=Color.RED))
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.font.color.rgb == "00FF0000"


@pytest.mark.parametrize(
    "alignment,expected_horizontal",
    [
        (AlignmentEnum.LEFT, "left"),
        (AlignmentEnum.CENTER, "center"),
        (AlignmentEnum.RIGHT, "right"),
        (AlignmentEnum.JUSTIFY, "justify"),
    ],
)
def test_convert_alignment_horizontal(alignment, expected_horizontal):
    style = get_fake_style(alignment=alignment)
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.alignment.horizontal == expected_horizontal


def test_convert_fill_with_color():
    style = get_fake_style(fill_color=Color.BLUE)
    openpyxl_style = OpenPyXLStyleAdapter.convert(style)
    assert openpyxl_style.fill.fill_type == "solid"
    assert openpyxl_style.fill.start_color.rgb == "000000FF"
