import sqlite3

from constants import DB_PATH
from models.authors import Author

sql_create_author = '''
INSERT INTO author (first_name, last_name)
VALUES (?, ?)
'''

# provjera da li autor sa istim imenom i prezimenom vec postoji u bazi
sql_get_author_by_name = '''
SELECT * FROM author
WHERE first_name LIKE ?
AND last_name LIKE ?   
'''


def get_author_by_name(first_name: str, last_name: str) -> Author | None:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_get_author_by_name, (first_name, last_name))
            row = cursor.fetchone()
            if row:
                author = Author(row[1], row[2])
                author.id = row[0]
                return author
    except Exception as ex:
        print(f"Dogodila se greska {ex}.")
        return None


def add_author(author: Author) -> int | None:
    if not isinstance(author, Author): # provjera da li je author instanca Author klase
        return None                    # ako nije, vrati None
    existing_author = get_author_by_name(author.first_name, author.last_name)   # provjera da li autor vec postoji u bazi
    if existing_author:                                                          # ako autor vec postoji, vrati njegov ID
        return existing_author.id
    try:
        with sqlite3.connect(DB_PATH) as conn:                                  # dodavanje novog autora u bazu
            cursor = conn.cursor()                                              # kreiranje kursora
            cursor.execute(sql_create_author, (author.first_name, author.last_name))    # izvrsavanje SQL upita za dodavanje autora
            return cursor.lastrowid                                    # vracanje ID-a novododanog autora
    except Exception as ex:                                       # hvatanje gresaka
        print(f"Dogodila se greska {ex}.")
        return None                                               # vracanje None u slucaju greske
