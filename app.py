# CRUD operacije nad podacina u bazi podataka
import sqlite3


DB_PATH = './datastore/baza.db'


# Knjiga ima jednog autora, a autor može imati više knjiga
class Book:
    def __init__(self, title: str, author: Authors, description: str = '', price: float, isbn: str):
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.isbn = isbn
    def __str__(self):
        return f'Naslov: {self.title}, ({self.author.full_name})'


# Autor može imati više knjiga
class Authors:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self._full_name()
    
    def _full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name}'

    def add_book(self, book: Book):
        self.books.append(book)
    

sql_create_tables = '''
CREATE TABLE IF NOT EXISTS author
(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS book
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NULL
    isbn TEXT NULL,
    price REAL NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) 
        REFERENCES author (id)
)
'''



try:
    with sqlite3.connect(DB_PATH) as conn:
        pass


except Exception as ex:
    print(f'Dogodila se greška:    {ex}.')
