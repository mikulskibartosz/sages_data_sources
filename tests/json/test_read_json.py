import pandas as pd


JSON_ARRAY = 'input_data/json/iris.json'
JSON_LINES = 'input_data/json/iris_lines.json'

def test_read_json():
    """Wczytaj zawartość pliku JSON_ARRAY jako Pandas DataFrame"""
    df = pd.read_json(JSON_ARRAY)

    print(df)
    assert df.shape == (30, 5)
    assert df.columns.to_list() == ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species']

def test_read_json_change_column_names():
    """Wczytaj zawartość pliku JSON_ARRAY jako Pandas DataFrame, zmieniając nazwy kolumn
    w następujący sposób:
    sepalLength -> sepal_length
    sepalWidth -> sepal_width
    petalLength -> petal_length
    petalWidth -> petal_width
    species -> species"""
    df = pd.read_json(JSON_ARRAY)
    df.rename(columns={'sepalLength': 'sepal_length', 'sepalWidth': 'sepal_width', 'petalLength': 'petal_length', 'petalWidth': 'petal_width'}, inplace=True)

    print(df)
    assert df.shape == (30, 5)
    assert df.columns.to_list() == ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

def test_read_json_lines():
    """Wczytaj zawartość pliku JSON_LINES jako Pandas DataFrame"""
    df = pd.read_json(JSON_LINES, lines=True)

    print(df)
    assert df.shape == (30, 5)
    assert df.columns.to_list() == ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species']
