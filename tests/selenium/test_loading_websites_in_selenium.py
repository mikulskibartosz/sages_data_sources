from selenium import webdriver
from selenium.webdriver.common import by
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
import pytest
import time
import pandas as pd

URL = 'https://github.com/mikulskibartosz/sages_data_sources/tree/rozwiazania/input_data/markdown'

def safari():
    return webdriver.Safari()

def firefox():
    return webdriver.Firefox(executable_path=GeckoDriverManager().install())

def chrome():
    return webdriver.Chrome(executable_path=ChromeDriverManager().install())

def edge():
    return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    
def opera():
    return webdriver.Opera(executable_path=OperaDriverManager().install())

@pytest.fixture(scope='function')
def driver():
    driver = safari()
    yield driver
    driver.quit()


def test_check_if_driver_works(driver):
    """To jest test sprawdzający czy Selenium zostało poprawnie zainstalowane."""
    driver.get(URL)
    assert driver.current_url == URL

def test_load_page_using_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Użyj selenium do wczytania tytułu strony.

    Podpowiedź: webdriver.Safari() jest wbudowany w selenium i nie wymaga dodatkowej instalacji.
    Ale trzeba mieć zainstalowane Safari w systemie.
    """
    driver.get(URL)
    title = driver.title
    print(title)
    assert 'mikulskibartosz/sages_data_sources' in title


def test_load_table_header_using_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Wczytaj nagłówki tabeli znajdujacej się na stronie (tej samej której używaliśmy w testach beautifulsoup)
    """
    driver.get(URL)
    headers = driver.find_elements(by=by.By.XPATH, value='//article/table/thead/tr/th')
    header_titles = [header.text for header in headers]

    print(header_titles)
    assert header_titles == ['kolumna_A', 'kolumna_B', 'kolumna_C']


def test_load_table_as_dataframe_using_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Wczytaj tabelę znajdujacą się na stronie jako Pandas DataFrame (tej samej której używaliśmy w testach beautifulsoup)
    """
    driver.get(URL)
    table = driver.find_elements(by=by.By.XPATH, value='//article/table')
    html = table[0].get_attribute('innerHTML')
    html = f'<table>{html}</table>'

    df = pd.read_html(html)[0]

    print(df)
    assert df.equals(pd.DataFrame({
        'kolumna_A': ['A1', 'B1', 'C1', 'D1'],
        'kolumna_B': ['A2', 'B2', 'C2', 'D2'],
        'kolumna_C': ['A3', 'B3', 'C3', 'D3'],
    }))


def test_follow_links_in_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Przejdź do strony page1 i wczytaj jej tytuł"""
    driver.get(URL)
    print(driver.title)
    print(driver.find_element(by=by.By.LINK_TEXT, value='page1').get_attribute('href'))
    driver.find_element(by=by.By.LINK_TEXT, value='page1').click()
    time.sleep(2)

    title = driver.title
    print(title)
    assert 'page1' in title
