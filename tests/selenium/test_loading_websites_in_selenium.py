from selenium import webdriver
import pytest

URL = 'https://github.com/mikulskibartosz/sages_data_sources/tree/rozwiazania/input_data/markdown'

@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Safari()
    yield driver
    driver.quit()

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