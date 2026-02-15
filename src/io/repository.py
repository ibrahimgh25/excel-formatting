from abc import ABC, abstractmethod
import os
from typing import Optional

import pandas as pd

from ..formats.styles.base import TableStyle
from ..table import Table

from .excel_read import read_excel_sheet
from .excel_write import save_dataframe_to_excel, create_style_dict


class TableNotFoundError(Exception):
    pass


class TableRepository(ABC):

    @abstractmethod
    def get_table(self, table_id: str) -> Table:
        pass

    @abstractmethod
    def save_table(
        self,
        table: Table,
        header_style: TableStyle | None = None,
        body_style: TableStyle | None = None,
        column_widths: list[float] | None = None,
    ) -> None:
        pass


class ExcelTableRepository(TableRepository):
    def __init__(self, directory: str):
        os.makedirs(directory, exist_ok=True)
        self.directory = directory
        self.table_info = self._get_table_info()

    def _get_table_info(self) -> dict[str, str]:
        info_path = os.path.join(self.directory, "table_info.csv")
        try:
            df = pd.read_csv(info_path)
            return df.set_index("id")["name"].to_dict()
        except (FileNotFoundError, KeyError):
            return {}

    def _save_table_info(self) -> None:
        info_path = os.path.join(self.directory, "table_info.csv")
        df = pd.DataFrame(
            list(self.table_info.items()), columns=["id", "name"]
        )
        df.to_csv(info_path, index=False)

    def get_table(self, table_id: str) -> Table:
        if table_id not in self.table_info:
            raise TableNotFoundError(f"Table with ID '{table_id}' not found.")
        table_path = os.path.join(self.directory, table_id + ".xlsx")
        if not os.path.exists(table_path):
            raise TableNotFoundError(f"Excel file not found: {table_path}")
        table_name = self.table_info[table_id]
        data = read_excel_sheet(table_path, table_name)
        return Table(name=table_name, id=table_id, data=data)

    def save_table(
        self,
        table: Table,
        header_style: TableStyle | None = None,
        body_style: TableStyle | None = None,
        column_widths: Optional[list[float]] = None,
    ) -> None:
        file_path = os.path.join(self.directory, table.id + ".xlsx")

        column_styles = None
        if header_style and body_style:
            column_styles = [
                create_style_dict(header_style.name, body_style.name)
                for _ in range(len(table.data.columns))
            ]

        save_dataframe_to_excel(
            df=table.data,
            file_path=file_path,
            sheet_name=table.name,
            column_styles=column_styles,
            column_widths=column_widths,
        )

        self.table_info[table.id] = table.name
        self._save_table_info()
