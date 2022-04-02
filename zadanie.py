# 1. Z bazy danych znajdującej się w pliku data/sql/titanic.db (w katalogu roboczym używanym wczoraj), pobierz dane wszystkich osób, które przeżyły katastrofę Titanica i w czasie katastrofy miały powyżej 35 lat.
# 2. Na stronie https://en.wikipedia.org/wiki/Passengers_of_the_Titanic znajdź wszystkie osoby, które przeżyły. Pobierz linki do stron Wikipedii o tych osobach.
# 3. Połącz dane z naszej bazy danych z danymi pobranymi z Wikipedii. Interesują nas tylko osoby znajdujące się w obu zbiorach danych (ich nazwiska zostały zapisane w identyczny sposób w obu listach).
# Dla każdej osoby:
# 3. Otwórz stronę Wikipedii o tej osobie.
# 4. Z prawej strony znajduje się prostokąt z podsumowaniem informacji o osobie. Pobierz z niego wszystkie dane.
# Po pobraniu wszystkich osób:
# 6. Zapisz dane z wikipedii i bazy danych w jednym pliku XLS. Dane o każdej osobie powinny znaleźć się w osobnej zakładce (nazwanej nazwiskiem i imieniem tej osoby).
# 7. Każda zakładka powinna zawierać dwie kolumny: nazwa atrybutu i wartość (bez nagłówków)

import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree

con = sqlite3.connect('data/sql/titanic.db')
query = """
select * from passengers p
join survivors s on p.PassengerId = s.PassengerId
join tickets t on t.PassengerId = p.PassengerId
where s.Survived = 1 and Age > 35
"""
try:
    titanic_df = pd.read_sql_query(query, con)
finally:
    con.close()

survivor_names = titanic_df['Name'].tolist()

wikipedia_url = 'https://en.wikipedia.org/wiki/Passengers_of_the_Titanic'
response = requests.get(wikipedia_url)
response_page = BeautifulSoup(response.text, 'html.parser')
dom_tree = etree.HTML(str(response_page))
xpath = ".//table//tr[contains(@style, 'background')]/td[1]/a"
found_elements = dom_tree.xpath(xpath)

people_urls = []

for element in found_elements:
    if element.text in survivor_names:
        tpl = (f"https://en.wikipedia.org/{element.attrib['href']}", element.text)
        people_urls.append(tpl)

dfs_to_save = []

for people_url, person_name in people_urls:
    response = requests.get(people_url)
    response_page = BeautifulSoup(response.text, 'html.parser')
    dom_tree = etree.HTML(str(response_page))
    xpath = "//table[contains(@class, 'infobox')]"
    found_elements = dom_tree.xpath(xpath)

    html = etree.tostring(found_elements[0], pretty_print=True)
    df = pd.read_html(html)[0]

    data_from_db = titanic_df[titanic_df['Name'] == person_name]
    data_from_db = data_from_db.transpose()
    data_from_db = data_from_db.reset_index()

    df.columns = ['Attribute', 'Value']
    data_from_db.columns = ['Attribute', 'Value']

    df = df.append(data_from_db)
    df = df[df['Attribute'] != 'index']
    dfs_to_save.append((df, person_name))

    writer = pd.ExcelWriter('output.xls', engine='xlsxwriter')
    for df, name in dfs_to_save:
        print(df)
        df.to_excel(writer, sheet_name=name, index=False)
    writer.save()
