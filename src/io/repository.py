from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd

from .excel_read import read_excel_sheet
from .excel_write import save_dataframe_to_excel, create_style_dict


class TableRepository(ABC):

    @abstractmethod
    def get_table(self, table_name: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def save_table(
        self,
        table_name: str,
        data: pd.DataFrame,
        column_styles: Optional[list[dict[str, str]]] = None,
        column_widths: Optional[list[float]] = None,
    ) -> None:
        pass


class ExcelTableRepository(TableRepository):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_table(self, table_name: str) -> pd.DataFrame:
        return read_excel_sheet(self.file_path, table_name)

    def save_table(
        self,
        table_name: str,
        data: pd.DataFrame,
        column_styles: Optional[list[dict[str, str]]] = None,
        column_widths: Optional[list[float]] = None,
    ) -> None:
        save_dataframe_to_excel(
            df=data,
            file_path=self.file_path,
            sheet_name=table_name,
            column_styles=column_styles,
            column_widths=column_widths,
        )

    def save_table_with_style(
        self,
        table_name: str,
        data: pd.DataFrame,
        header_style: str = "BlueHeaderCentered",
        body_style: str = "BodyCentered",
        column_widths: Optional[list[float]] = None,
    ) -> None:
        column_styles = [
            create_style_dict(header_style, body_style)
            for _ in range(len(data.columns))
        ]

        self.save_table(table_name, data, column_styles, column_widths)
