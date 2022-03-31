import os
import pandas as pd
import pytest


EXCEL_TO_BE_SAVED = 'data/excel/excel_to_be_saved.xlsx'
SHEET_1 = 'Sheet1'
SHEET_2 = 'Sheet2'

ROWS = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

HEADERS = ['col1', 'col2', 'col3']

def test_save_list_as_excel():
    """
    Stwórz DataFrame zawierający dane z listy ROWS używając nagłówków HEADERS.
    Zapisz ten DataFrame w pliku Excel (użyj zmiennej EXCEL_TO_BE_SAVED).

    Plik powinien zawierać zakładkę SHEET_1 oraz zakładkę SHEET_2.
    W obu zakładkach zapisujemy ten same DataFrame.
    """
    df = ...
    print(df)
    assert df.equals(
        pd.DataFrame(
            {
                "col1": ['a', 'd', 'g'],
                "col2": ['b', 'e', 'h'],
                "col3": ['c', 'f', 'i'],
            }
        )
    )

    df = pd.read_excel(EXCEL_TO_BE_SAVED, sheet_name=SHEET_2)
    print(df)
    assert df.equals(
        pd.DataFrame(
            {
                "col1": ['a', 'd', 'g'],
                "col2": ['b', 'e', 'h'],
                "col3": ['c', 'f', 'i'],
            }
        )
    )