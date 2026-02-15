import pandas as pd
from dataclasses import dataclass


@dataclass
class Table:
    name: str
    id: str
    data: pd.DataFrame

    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def columns(self) -> int:
        return len(self.data.columns)
