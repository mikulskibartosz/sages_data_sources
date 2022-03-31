import os
import pandas as pd
import pytest
import sqlite3

"""Ttanic dataset
survival	Survival	0 = No, 1 = Yes
pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
sex	Sex
Age	Age in years
sibsp	# of siblings / spouses aboard the Titanic
parch	# of parents / children aboard the Titanic
ticket	Ticket number
fare	Passenger fare
cabin	Cabin number
embarked	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton
"""

DATABASE_PATH = 'data/sql/titanic.db'

def run_query(query):
    con = sqlite3.connect(DATABASE_PATH)
    try:
        response = pd.read_sql_query(query, con)
        return response
    finally:
        con.close()

class TestSql:

    @pytest.fixture(scope='class')
    def test_directory(self):
        os.makedirs('data/sql/', exist_ok=True)

    @pytest.fixture(scope="class")
    def load_titanic_data(self, test_directory):
        titanic_data = pd.read_csv('input_data/sql/titanic.csv')

        survivors = titanic_data[['PassengerId', 'Survived']]
        tickets = titanic_data[['PassengerId', 'Ticket', 'Pclass', 'Fare', 'Cabin', 'Embarked']]
        passengers = titanic_data[['PassengerId', 'Name', 'Sex', 'Age', 'SibSp', 'Parch']]

        con = sqlite3.connect(DATABASE_PATH)
        try:
            survivors.to_sql('survivors', con, if_exists='replace')
            tickets.to_sql('tickets', con, if_exists='replace')
            passengers.to_sql('passengers', con, if_exists='replace')
        finally:
            con.close()

    def test_load_passenger_names(self, load_titanic_data):
        """Wczytaj nazwiska pasażerów z tabeli passengers.
        Podpowiedź: użyj funkcji run_query
        """
        df = run_query('SELECT Name FROM passengers')

        print(df)
        assert df.columns.values == ['Name']
        names = df.Name.tolist()
        assert 'Braund, Mr. Owen Harris' in names
        assert 'Montvila, Rev. Juozas' in names

    def test_load_passengers_by_sex_and_age(self, load_titanic_data):
        """Wczytaj nazwisko kobiet mających powyżej 60 lat z listy pasażerów."""
        df = run_query("SELECT Name FROM passengers WHERE Sex='female' and Age > 60")

        print(df)
        assert df.columns.values == ['Name']
        names = df.Name.tolist()
        assert 'Andrews, Miss. Kornelia Theodosia' in names

    def test_sort_passengers_by_age(self, load_titanic_data):
        """Wczytaj nazwiska pasażerów. Posortuj wyniki wg wieku (rosnąco).
        Pomiń osoby, których wiek jest nieznany."""
        df = run_query("SELECT Name FROM passengers WHERE Age is not null ORDER BY Age")

        print(df)
        assert df.columns.values == ['Name']
        names = df.Name.tolist()
        assert 'Thomas, Master. Assad Alexander' == names[0]
        assert 'Hamalainen, Master. Viljo' == names[1]

    def test_find_the_oldest_passenger(self, load_titanic_data):
        """Wczytaj nazwisko najstarszego pasażera. Zwróc tylko jedną wartość."""
        df = run_query("SELECT Name FROM passengers WHERE Age is not null ORDER BY Age DESC LIMIT 1")

        print(df)
        assert df.shape == (1, 1)
        assert df.columns.values == ['Name']
        names = df.Name.tolist()
        assert 'Barkworth, Mr. Algernon Henry Wilson' == names[0]

    def test_find_survivors(self, load_titanic_data):
        """Wczytaj nazwiska osób które przeżyły zatonięcie Titanica."""
        df = run_query("SELECT p.Name as Name FROM passengers p JOIN survivors s ON p.PassengerId = s.PassengerId WHERE s.Survived = 1")

        print(df)
        assert df.columns.values == ['Name']
        names = df.Name.tolist()
        assert 'Heikkinen, Miss. Laina' in names
        assert 'Moran, Mr. James' not in names

    def test_count_by_embarked(self, load_titanic_data):
        """Policz liczbę osób które rozpoczęły podróż w każdym z portów (kolumna embarked).
        Pomiń osoby z nieznanym portem.
        Zwróc dwie kolumny: embarked oraz number_of_passengers."""
        df = run_query("SELECT Embarked as embarked, count(*) as number_of_passengers FROM passengers p JOIN tickets t ON p.PassengerId = t.PassengerId WHERE Embarked is not null GROUP BY Embarked")

        print(df)
        assert df.shape == (3, 2)
        assert df.embarked.tolist() == ['C', 'Q', 'S']
        assert df.number_of_passengers.tolist() == [168, 77, 644]

    def test_find_max_min_age_by_sex_and_survived(self, load_titanic_data):
        """
        Pogrupuj dane wg kolumn Sex oraz Survived. W każdej grupie znajdź wiek najstarszej i najmłodszej osoby.
        Wynik powinien zawierać cztery kolumny: Sex, Survived, Oldest, Youngest
        """
        df = run_query("""
        SELECT Sex, Survived, max(Age) as Oldest, min(Age) as Youngest FROM passengers p JOIN survivors s ON p.PassengerId = s.PassengerID WHERE Age is not null GROUP BY Sex, Survived
        """)

        print(df)
        assert df.equals(
            pd.DataFrame({
                'Sex': ['female', 'female', 'male', 'male'],
                'Survived': [0, 1, 0, 1],
                'Oldest': [57.0, 63.0, 74.0, 80.0],
                'Youngest': [2.0, 0.75, 1.0, 0.42]
            })
        )