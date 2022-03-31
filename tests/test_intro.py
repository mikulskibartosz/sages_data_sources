# wszystkie importy używane w czasie zadań
import pytest
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common import by
import sqlite3

class TestIntro:
    @pytest.fixture(scope='class')
    def kod_wykonany_przed_wszystkimi_testami(self):
        print('Przed testem')
        return ['a', 'b', 'c']

    def test_z_fixture(self, kod_wykonany_przed_wszystkimi_testami):
        print('Test z fixture')
        assert kod_wykonany_przed_wszystkimi_testami == ['a', 'b', 'c']

    def test_dodawanie(self):
        wynik = 1 + 1
        assert wynik == 2
