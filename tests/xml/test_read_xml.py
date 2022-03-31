"""
Zadania z książki innego trenera Sages - Matt Harasymczuk
https://python.astrotech.io/pandas/import-export/read-xml.html
"""

import pandas as pd

DATA = """<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
   </book>
   <book id="bk103">
      <author>Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology society in England, the young survivors lay the foundation for a new society.</description>
   </book>
</catalog>
"""

DATA_WITH_AUTHORS = """<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>
        <last_name>Gambardella</last_name>
        <first_name>Matthew</first_name>
      </author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications with XML.</description>
   </book>
   <book id="bk102">
      <author>
        <last_name>Ralls</last_name>
        <first_name>Kim</first_name>
      </author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
   </book>
   <book id="bk103">
      <author>
        <last_name>Corets</last_name>
        <first_name>Eva</first_name>
      </author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology society in England, the young survivors lay the foundation for a new society.</description>
   </book>
</catalog>
"""

def test_read_xml():
    """Wczytaj zawartość zmiennej DATA jako Pandas DataFrame."""
    df = pd.read_xml(DATA)

    print(df)
    assert df.equals(
        pd.DataFrame(
            {
                "id": ["bk101", "bk102", "bk103"],
                "author": ["Gambardella, Matthew", "Ralls, Kim", "Corets, Eva"],
                "title": ["XML Developer's Guide", "Midnight Rain", "Maeve Ascendant"],
                "genre": ["Computer", "Fantasy", "Fantasy"],
                "price": [44.95, 5.95, 5.95],
                "publish_date": ["2000-10-01", "2000-12-16", "2000-11-17"],
                "description": [
                    "An in-depth look at creating applications with XML.",
                    "A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.",
                    "After the collapse of a nanotechnology society in England, the young survivors lay the foundation for a new society."
                ]
            }
        )
    )

def test_read_authors_from_xml():
    """Wczytaj tylko autorów książek ze zmiennej DATA_WITH_AUTHORS jako Pandas DataFrame.
    Podpowiedź: użyj argumentu xpath.
    """
    df = pd.read_xml(DATA_WITH_AUTHORS, xpath=".//book/author")

    print(df)
    assert df.equals(
        pd.DataFrame(
            {
                "last_name": ["Gambardella", "Ralls", "Corets"],
                "first_name": ["Matthew", "Kim", "Eva"]
            }
        )
    )

def test_read_fantasy_books():
    """Zwróć tylko książki Fantasy ze zmiennej DATA"""
    df = pd.read_xml(DATA, xpath=".//book[genre='Fantasy']")

    print(df)
    assert df.equals(
        pd.DataFrame(
            {
                "id": ["bk102", "bk103"],
                "author": ["Ralls, Kim", "Corets, Eva"],
                "title": ["Midnight Rain", "Maeve Ascendant"],
                "genre": ["Fantasy", "Fantasy"],
                "price": [5.95, 5.95],
                "publish_date": ["2000-12-16", "2000-11-17"],
                "description": [
                    "A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.",
                    "After the collapse of a nanotechnology society in England, the young survivors lay the foundation for a new society."
                ]
            }
        )
    )
