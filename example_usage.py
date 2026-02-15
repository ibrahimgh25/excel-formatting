import json
import pandas as pd

from src.io.repository import ExcelTableRepository
from src.table import Table
from src.formats.styles.builtin import BLUE_HEADER_CENTERED, BODY_CENTERED, BODY_LEFT

SAMPLE_DATA_PATH = ".assets/samples/sample_data.json"
OUTPUT_DIR = "example_output"


def load_sample_data() -> dict:
    with open(SAMPLE_DATA_PATH) as f:
        return json.load(f)


def example_save_tables(repo: ExcelTableRepository):
    data = load_sample_data()

    sales_table = Table(
        name="Sales",
        id="quarterly_sales",
        data=pd.DataFrame(data["quarterly_sales"]),
    )
    repo.save_table(
        table=sales_table,
        header_style=BLUE_HEADER_CENTERED,
        body_style=BODY_CENTERED,
        column_widths=[12, 10, 12, 12, 12],
    )
    print(f"Saved '{sales_table.name}' table ({sales_table.size} rows, {sales_table.columns} cols)")

    employees_table = Table(
        name="Employees",
        id="employees",
        data=pd.DataFrame(data["employees"]),
    )
    repo.save_table(
        table=employees_table,
        header_style=BLUE_HEADER_CENTERED,
        body_style=BODY_LEFT,
        column_widths=[20, 16, 22, 12, 14, 30],
    )
    print(f"Saved '{employees_table.name}' table ({employees_table.size} rows, {employees_table.columns} cols)")


def example_read_tables(repo: ExcelTableRepository):
    for table_id in repo.table_info:
        table = repo.get_table(table_id)
        print(f"\n--- {table.name} (id={table.id}, {table.size} rows) ---")
        print(table.data.head())


if __name__ == "__main__":
    print("=== Excel Formatting Examples ===\n")

    repo = ExcelTableRepository(OUTPUT_DIR)

    print("1) Saving tables via repository")
    example_save_tables(repo)
    print()

    print("2) Reading tables back via repository")
    example_read_tables(repo)
