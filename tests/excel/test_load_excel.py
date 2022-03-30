import os
import pandas as pd
import pytest

EXCEL_WITH_HEADER = 'data/excel/excel_with_headers.xlsx'
EXCEL_WITH_SHEET = 'data/excel/excel_with_sheet.xlsx'
EXCEL_WITH_TYPES = 'data/excel/excel_with_types.xlsx'
SHEET_TO_BE_IGNORED = 'Sheet1'
SHEET_TO_BE_LOADED = 'Sheet2'

class TestLoadExcel:
    @pytest.fixture(scope='class')
    def test_directory(self):
        os.makedirs('data/excel/', exist_ok=True)

    @pytest.fixture(scope="class")
    def excel_with_header(self, test_directory):
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": [4, 5, 6],
                "col3": [7, 8, 9],
            }
        )
        df.to_excel(EXCEL_WITH_HEADER, index=False)

    @pytest.fixture(scope="class")
    def excel_with_multiple_sheets(self, test_directory):
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": [4, 5, 6],
                "col3": [7, 8, 9],
            }
        )
        df2 = pd.DataFrame(
            {
                "col1": [10, 20, 30],
                "col2": ['A', 'B', 'C']
            }
        )

        writer = pd.ExcelWriter(EXCEL_WITH_SHEET, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=SHEET_TO_BE_IGNORED, index=False)
        df2.to_excel(writer, sheet_name=SHEET_TO_BE_LOADED, index=False)
        writer.save()

    @pytest.fixture(scope="class")
    def excel_with_types(self, test_directory):
        df = pd.DataFrame(
            {
                "col1": ['2022-04-02', '2022-04-03', '2022-04-04'],
                "col2": ['11:15', '11:30', '11:45'],
                "col3": [7, 8, 9],
            }
        )
        df.to_excel(EXCEL_WITH_TYPES, index=False)

    def test_load_excel_file_with_headers(self, excel_with_header):
        """
        Wczytaj plik xlsx EXCEL_WITH_HEADER.
        """
        df = pd.read_excel(EXCEL_WITH_HEADER)

        print(df)
        assert df.equals(
            pd.DataFrame(
                {
                    "col1": [1, 2, 3],
                    "col2": [4, 5, 6],
                    "col3": [7, 8, 9],
                }
            )
        )

    def test_load_sheet_from_excel(self, excel_with_multiple_sheets):
        """
        Wczytaj zakładkę z nazwą znajdującą się w zmiennej SHEET_TO_BE_LOADED
        z pliku xlsx EXCEL_WITH_SHEET.
        """
        df = pd.read_excel(EXCEL_WITH_SHEET, sheet_name=SHEET_TO_BE_LOADED)

        print(df)
        assert df.equals(
            pd.DataFrame(
                {
                    "col1": [10, 20, 30],
                    "col2": ['A', 'B', 'C']
                }
            )
        )

    def test_load_excel_with_types(self, excel_with_types):
        """
        Wczytaj plik EXCEL_WITH_TYPES.
        Kolumna col1 powinna zawierać datę (typ datetime).
        Kolumna col2 powinna zawierać tekst (typ str).
        Kolumna col3 powinna zawierać liczbę (typ int).
        """
        df = pd.read_excel(EXCEL_WITH_TYPES, dtype={'col1': 'datetime64[ns]'})

        print(df.col1.dtype)
        assert df.col1.dtype == 'datetime64[ns]'

        print(df.col2.dtype)
        assert df.col2.dtype == 'object'

        print(df.col3.dtype)
        assert df.col3.dtype == 'int64'

        print(df)
        assert df.equals(
            pd.DataFrame(
                {
                    "col1": [pd.Timestamp('2022-04-02'), pd.Timestamp('2022-04-03'), pd.Timestamp('2022-04-04')],
                    "col2": ['11:15', '11:30', '11:45'],
                    "col3": [7, 8, 9],
                }
            )
        )