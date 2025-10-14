import pandas as pd
import numpy as np
from src.io.repository import ExcelTableRepository
from src.io.excel_write import create_style_dict


def example_repository_usage():
    np.random.seed(42)
    df = pd.DataFrame(
        {
            "Column1": np.random.randint(0, 100, size=20),
            "Column2": np.random.randint(0, 100, size=20),
            "Column3": ["A", "B", "C"] * 6 + ["A", "B"],
        }
    )

    repo = ExcelTableRepository("example_output.xlsx")

    repo.save_table_with_style(
        table_name="SimpleSheet",
        data=df,
        header_style="BlueHeaderCentered",
        body_style="BodyCentered",
        column_widths=[15, 15, 20],
    )

    column_styles = [
        create_style_dict("BlueHeaderCentered", "BodyCentered"),
        create_style_dict("BlueHeaderCentered", "BodyCentered"),
        create_style_dict("BlueHeaderCentered", "BodyLeft"),
    ]

    repo.save_table(
        table_name="CustomSheet",
        data=df,
        column_styles=column_styles,
        column_widths=[15, 15, 25],
    )

    print("✓ Saved data to example_output.xlsx")

    df_read = repo.get_table("SimpleSheet")
    print(f"✓ Read {len(df_read)} rows from SimpleSheet")
    print(df_read.head())


def example_direct_usage():
    from src.io.excel_write import save_dataframe_to_excel
    from src.io.excel_read import read_excel_sheet, get_sheet_names

    df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Score": [95, 87, 92, 88],
            "Grade": ["A", "B", "A", "B"],
        }
    )

    save_dataframe_to_excel(
        df=df,
        file_path="direct_example.xlsx",
        sheet_name="Students",
        column_styles=[
            create_style_dict("BlueHeaderCentered", "BodyLeft"),
            create_style_dict("BlueHeaderCentered", "BodyCentered"),
            create_style_dict("BlueHeaderCentered", "BodyCentered"),
        ],
        column_widths=[20, 15, 15],
    )

    print("✓ Saved data to direct_example.xlsx")

    df_read = read_excel_sheet("direct_example.xlsx", "Students")
    print(f"✓ Read {len(df_read)} rows")

    sheets = get_sheet_names("direct_example.xlsx")
    print(f"✓ Available sheets: {sheets}")


def example_multiple_sheets():
    repo = ExcelTableRepository("multi_sheet_example.xlsx")

    sales_df = pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Revenue": [10000, 12000, 15000, 13000],
            "Profit": [2000, 2500, 3000, 2800],
        }
    )

    repo.save_table_with_style(
        table_name="Sales",
        data=sales_df,
        header_style="BlueHeaderCentered",
        body_style="BodyCentered",
        column_widths=[15, 15, 15],
    )

    employee_df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie"],
            "Department": ["Engineering", "Sales", "Marketing"],
            "Email": ["alice@company.com", "bob@company.com", "charlie@company.com"],
        }
    )

    repo.save_table(
        table_name="Employees",
        data=employee_df,
        column_styles=[
            create_style_dict("BlueHeaderCentered", "BodyLeft"),
            create_style_dict("BlueHeaderCentered", "BodyCentered"),
            create_style_dict("BlueHeaderCentered", "CustomHyperlink"),
        ],
        column_widths=[20, 20, 30],
    )

    print("✓ Created multi_sheet_example.xlsx with Sales and Employees sheets")


if __name__ == "__main__":
    print("Running Excel formatting examples...\n")

    print("Example 1: Repository pattern usage")
    example_repository_usage()
    print()

    print("Example 2: Direct function usage")
    example_direct_usage()
    print()

    print("Example 3: Multiple sheets")
    example_multiple_sheets()
    print()

    print("All examples completed successfully! 🎉")
