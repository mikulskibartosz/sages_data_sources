import pandas as pd


DATA = pd.DataFrame(
    {
        "col1": [3, 2, 1],
        "col2": ['Trzeci', 'Drugi', 'Pierwszy'],
        "col3": ['AAA', 'AAA', 'AAA'],
    }
)

EMPLOYEES = pd.DataFrame({
    'first_name': ['John', 'Jane', 'Mary', 'Mark', 'Mike', 'Alice'],
    'last_name': ['Smith', 'Doe', 'Jane', 'Twain', 'Tyson', 'Doe']
})

SALES = df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})

# generate a list of sales data containing 20 rows
SALES_LONG = pd.DataFrame({
    'year': [2012, 2012, 2014, 2014, 2013, 2015, 2012, 2021, 2015, 2018, 2021, 2015],
    'sale': [5, 40, 84, 31, 55, 40, 90, 31, 55, 40, 84, 31]
})

def test_sort_values_by_column():
    """Dany jest DataFrame DATA.
    Posortuj jego zawartość wg kolumny co1 rosnąco.

    Podpowiedź:
    Po posortowaniu index będzie w odwrotnej kolejności. Najlepiej go usunąć.
    """
    df = ...
    print(df)

    assert df.equals(
        pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": ['Pierwszy', 'Drugi', 'Trzeci'],
                "col3": ['AAA', 'AAA', 'AAA'],
            }
        )
    )

def test_sort_by_multiple_columns():
    """
    Posortuj DataFrame EMPLOYEES wg kolumn last_name w kolejności odwrotnej i first_name w kolejności alfabetycznej.
    """
    df = ...
    print(df)

    assert df.equals(
        pd.DataFrame({
            'first_name': ['Mike', 'Mark', 'John', 'Mary', 'Alice', 'Jane'],
            'last_name': ['Tyson', 'Twain', 'Smith', 'Jane', 'Doe', 'Doe']
        })
    )

def test_create_index():
    """Użyj kolumny col1 jako index DataFrame DATA."""
    df = ...
    print(df)

    assert df.index.equals(pd.Index([3, 2, 1]))

def test_create_text_index():
    """Użyj kolumny tekstowej col2 jako index DataFrame DATA."""
    df = ...
    print(df)

    assert df.index.equals(pd.Index(['Trzeci', 'Drugi', 'Pierwszy']))

def test_create_multiindex():
    """Użyj kolumn year, month aby stworzyć index DataFrame SALES"""
    df = ...
    print(df)

    expected_index = pd.MultiIndex.from_tuples([(2012, 1), (2014, 4), (2013, 7), (2014, 10)], names=['year', 'month'])
    assert df.index.equals(expected_index)

def test_group_by_and_sum():
    """
    Stwórz DataFrame zawierający sumę sprzedaży wg roku z danych SALES.

    Podpowiedź:
    Usuń kolumnę month z wyniku.
    """
    df = ...
    print(df)

    expected_df = pd.DataFrame({'sale': [55, 84, 71]}, index=[2012, 2013, 2014])
    expected_df.index.name = 'year'
    assert df.equals(expected_df)

def test_group_by_and_mean():
    """
    Stwórz DataFrame zawierający średnią sprzedaż wg roku z danych SALES_LONG.
    """
    df = ...
    print(df)

    expected_df = pd.DataFrame({'sale': [45.0, 55.0, 57.5, 42.0, 40.0, 57.5]}, index=[2012, 2013, 2014, 2015, 2018, 2021])
    expected_df.index.name = 'year'
    assert df.equals(expected_df)

def test_group_by_and_agg():
    """
    Oblicz sumę i średnią sprzedaży wg roku z danych SALES_LONG używając tylko jednej operacji grupowania.
    """
    df = ...
    print(df)

    expected_df = pd.DataFrame({
        'sum': [135, 55, 115, 126, 40, 115],
        'mean': [45.0, 55.0, 57.5, 42.0, 40.0, 57.5]
    }, index=[2012, 2013, 2014, 2015, 2018, 2021])
    expected_df.columns = pd.MultiIndex.from_product([['sale'], expected_df.columns])
    expected_df.index.name = 'year'
    assert df.equals(expected_df)