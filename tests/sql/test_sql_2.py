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

DATABASE_PATH = 'data/sql/titanic_2.db'

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
        tickets = tickets.drop(tickets.index[::2])
        passengers = titanic_data[['PassengerId', 'Name', 'Sex', 'Age', 'SibSp', 'Parch']]

        con = sqlite3.connect(DATABASE_PATH)
        try:
            survivors.to_sql('survivors', con, if_exists='replace')
            tickets.to_sql('tickets', con, if_exists='replace')
            passengers.to_sql('passengers', con, if_exists='replace')
        finally:
            con.close()

    def test_load_passengers_without_tickets(self, load_titanic_data):
        """Wczytaj nazwiska pasażerów bez biletów z tabeli passengers.
        Podpowiedź: użyj funkcji run_query
        """
        df = run_query('...')

        print(df)
        assert df.columns.values == ['Name']
        names = df.Name.tolist()
        assert 'Braund, Mr. Owen Harris' in names
        assert 'Montvila, Rev. Juozas' in names
        assert 'Moran, Mr. James' not in names

    def test_load_passengers_and_their_cabin_numbers_keep_passengers_without_tickets(self, load_titanic_data):
        """Wczytaj nazwiska i numery kabin wszystkich pasażerów. Jeśli osoba nie ma biletu (lub ma bilet bez kabiny), pozostaw pustą wartość w kolumnie Cabin.
        """
        df = run_query("...")

        print(df)
        values = df.values.tolist()
        assert ['Braund, Mr. Owen Harris', None] in values
        assert ['Graham, Miss. Margaret Edith', 'B42'] in values

    def test_load_passengers_and_their_ticket_numbers_remove_passengers_without_tickets(self, load_titanic_data):
        """Wczytaj nazwiska i numery biletów wszystkich pasażerów. Jeśli osoba nie ma biletu, usuń ją z listy.
        """
        df = run_query("...")

        print(df)
        values = df.values.tolist()
        for value in values:
            assert value[1] is not None
