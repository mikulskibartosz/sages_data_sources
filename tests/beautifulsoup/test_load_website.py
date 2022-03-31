import pandas as pd
from bs4 import BeautifulSoup
import requests

URL = 'https://github.com/mikulskibartosz/sages_data_sources/tree/rozwiazania/input_data/markdown'

def test_load_page_title():
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki requests.
    Użyj beautifulsoup do wczytania tytułu strony.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(title)
    assert 'mikulskibartosz/sages_data_sources' in title

def test_load_table_as_dataframe():
    """Wczytaj stronę ze zmiennej URL.
    Na stronie znajduje się tabelka. Wczytaj ją jako dataframe.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    table = article.find('table')
    table_html = table.prettify()
    dfs = pd.read_html(table_html)
    df = dfs[0]
    print(df)

    assert df.equals(pd.DataFrame({
        'kolumna_A': ['A1', 'B1', 'C1', 'D1'],
        'kolumna_B': ['A2', 'B2', 'C2', 'D2'],
        'kolumna_C': ['A3', 'B3', 'C3', 'D3'],
    }))

def test_load_multiple_pages():
    """Wczytaj stronę ze zmiennej URL.
    Na stronie znajdują się dwa linki page1 oraz page2. Wczytaj obie strony do których prowadzą te linki.
    Każda z tych stron zawiera tabelkę. Wczytaj obie tabelki i złącz ich zawartość w jeden DataFrame.

    Podpowiedź:
    Użyj reset_index() aby numerowanie wierszy było spójne z oczekiwanym wynikiem.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    pages_to_download = [link for link in links if link.string in ['page1', 'page2']]

    urls = ['https://github.com' + link.get('href') for link in pages_to_download]

    dfs = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article')
        table = article.find('table')
        table_html = table.prettify()
        dfs.append(pd.read_html(table_html)[0])

    df = pd.concat(dfs).reset_index(drop=True)
    print(df)

    assert df.equals(pd.DataFrame({
        'kolumna_A': ['A1', 'B1', 'C1', 'D1'],
        'kolumna_B': ['A2', 'B2', 'C2', 'D2'],
        'kolumna_C': ['Test1', 'Test2', 'Test3', 'Test4'],
    }))
