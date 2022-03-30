import pandas as pd


CSV_TO_BE_SAVED = 'data/csv/csv_to_be_saved.csv'

ROWS = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

HEADERS = ['col1', 'col2', 'col3']


def test_save_list_as_csv():
    """
    Zapisz listę ROWS w pliku CSV (użyj zmiennej CSV_TO_BE_SAVED).
    Użyj nagłówków z listy HEADERS.
    """
    df = pd.DataFrame(ROWS)
    df.to_csv(CSV_TO_BE_SAVED, index=False, header=HEADERS)

    df = pd.read_csv(CSV_TO_BE_SAVED)
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
