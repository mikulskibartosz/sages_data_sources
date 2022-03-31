import os
import pytest
import pandas as pd


CSV_WITH_HEADERS = 'data/csv/csv_with_headers.csv'
CSV_WITHOUT_HEADERS = 'data/csv/csv_without_headers.csv'
CSV_WITH_TEXT = 'data/csv/csv_with_text.csv'
POLISH_CSV = 'data/csv/polish_csv.csv'

class TestLoadCsv:
    @pytest.fixture(scope='class')
    def test_directory(self):
        os.makedirs('data/csv/', exist_ok=True)

    @pytest.fixture(scope="class")
    def csv_with_header(self, test_directory):
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": [4, 5, 6],
                "col3": [7, 8, 9],
            }
        )
        df.to_csv(CSV_WITH_HEADERS, index=False)

    @pytest.fixture(scope="class")
    def csv_without_header(self, test_directory):
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": [4, 5, 6],
                "col3": [7, 8, 9],
            }
        )
        df.to_csv(CSV_WITHOUT_HEADERS, index=False, header=False)

    @pytest.fixture(scope="class")
    def csv_with_text_before_table(self):
        text_before_table = """To jest plik testowy.

        Zawierający trzy wiersze opisu."""
        with open(CSV_WITH_TEXT, 'w') as f:
            f.write(text_before_table)
            f.write('\n')

        df = pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": [4, 5, 6],
                "col3": [7, 8, 9],
            }
        )
        df.to_csv(CSV_WITH_TEXT, index=False, mode='a')

    @pytest.fixture(scope="class")
    def polish_csv(self):
        df = pd.DataFrame(
            {
                "col1": [1.1, 2.2, 3.5],
                "col2": [4, 5, 6],
                "col3": [7, 8, 9],
            }
        )
        df.to_csv(POLISH_CSV, index=False, sep=';', decimal=',')

    def test_load_csv_with_headers(self, csv_with_header):
        """
        Wczytaj plik csv z nagłówkami używając funkcji pd.read_csv.
        Nazwa zmiennej ze ścieżką do pliku: CSV_WITH_HEADERS
        """
        df = ...

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

    def test_load_csv_without_headers(self, csv_without_header):
        """
        Wczytaj plik csv bez nagłówków używając funkcji pd.read_csv.
        Jako nazw kolumn użyj: col1, col2, col3

        Nazwa zmiennej ze ścieżką do pliku: CSV_WITHOUT_HEADERS
        """
        df = ...

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

    def test_change_header_names(self, csv_with_header):
        """
        Wczytaj plik zawierający nagłówki, ale zmień ich nazwy na col_A, col_B, col_C.
        Nazwa zmiennej ze ścieżką do pliku: CSV_WITH_HEADERS
        """
        df = ...

        print(df)
        assert df.equals(
            pd.DataFrame(
                {
                    "col_A": [1, 2, 3],
                    "col_B": [4, 5, 6],
                    "col_C": [7, 8, 9],
                }
            )
        )

    def test_change_column_types(self, csv_with_header):
        """
        Wczytaj plik zawierający nagłówki. Zmień typ kolumny col2 na string.
        Nazwa zmiennej ze ścieżką do pliku: CSV_WITH_HEADERS
        """
        df = ...

        print(df)
        assert df.equals(
            pd.DataFrame(
                {
                    "col1": [1, 2, 3],
                    "col2": ["4", "5", "6"],
                    "col3": [7, 8, 9],
                }
            )
        )

    def test_ignore_text_before_data(self, csv_with_text_before_table):
        """
        Wczytaj plik CSV_WITH_TEXT. Plik wygląda w taki sposób:
        ---
        To jest plik testowy.

        Zawierający trzy wiersze opisu.
        col1,col2,col3
        1,4,7
        2,5,8
        3,6,9
        ---
        W czasie wczytywania pliku zignoruj tekst znajdujący się przed danymi.
        """
        df = ...

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

    def test_load_csv_in_Polish_format(sefl, polish_csv):
        """
        Wczytaj plik POLISH_CSV.
        Ten plik zawiera dane w formacie CSV stosowanym w Polsce:
        * pola oddzielone średnikami
        * przecinek jako separator dziesiętny
        """
        df = ...

        print(df)
        assert df.equals(
            pd.DataFrame(
                {
                    "col1": [1.1, 2.2, 3.5],
                    "col2": [4, 5, 6],
                    "col3": [7, 8, 9],
                }
            )
        )
