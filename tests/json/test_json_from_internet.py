import pandas as pd
import pytest
import requests

URL = 'https://raw.githubusercontent.com/mikulskibartosz/sages_data_sources/rozwiazania/input_data/json/iris_lines.json'

@pytest.fixture(scope='class')
def expected_data():
    return pd.read_json('input_data/json/iris_lines.json', lines=True)

def test_load_json_from_internet_using_pandas(expected_data):
    """Używająć Pandas, wczytaj plik JSON znajdujący się pod adresem wskazanym przez zmienną URL.
    Podpowiedź: zawartość tego pliku jest taka sama jak input_data/json/iris_lines.json
    """
    df = ...
    print(df)

    assert df.equals(expected_data)

def test_load_json_using_requests(expected_data):
    """Używając biblioteki requests, wczytaj plik JSON znajdujący się pod adresem wskazanym przez zmienną URL.
    Podpowiedź: zawartość tego pliku jest taka sama jak input_data/json/iris_lines.json"""
    df = ...
    print(df)

    assert df.equals(expected_data)