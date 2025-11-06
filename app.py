import sqlite3

from models.authors import Author
from models.books import Book


DB_PATH = './data_store/baza.db'

sql_create_table_author = '''
CREATE TABLE IF NOT EXISTS author
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
'''
sql_create_table_book = '''
CREATE TABLE IF NOT EXISTS book
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NULL,
    isbn TEXT NULL,
    price REAL NOT NULL,
    author_id INTEGER NOT NULL,

    FOREIGN KEY (author_id)
        REFERENCES author (id)
);
'''
sql_create_author = '''
INSERT INTO author (first_name, last_name)
VALUES (?, ?)
'''
sql_create_book = '''
INSERT INTO book (title, description, isbn, price, author_id)
VALUES (?, ?, ?, ?, ?)
'''

def db_init():
    try:
        # with automatski zatvara konekciju (conn.close()) i radi commit (conn.commit())
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_table_author)
            cursor.execute(sql_create_table_book)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def add_author(author: Author) -> int:
    if isinstance(author, Author):
        params = (author.first_name, author.last_name)
    else:
        return

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_author, params)
            return cursor.lastrowid


    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def add_book(book: Book):
    if isinstance(book, Book):
        params = (book.title, book.description, book.isbn, book.price, book.author.id)
    else:
        return

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_book, params)
            return cursor.lastrowid


    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def main():
    # Kreiraj autora
    first_name = input('Upiste ime autora: ')
    last_name = input('Upiste prezime autora: ')
    author = Author(first_name, last_name)
    author.id = add_author(author)

    title = input('Upiste naziv knjige: ')
    description = input('Upiste kratki opis knjige: ')
    isbn = input('Upiste ISBN knjige: ')
    price = float(input('Upiste cijenu knjige: '))
    book = Book(title, author, price, description, isbn)
    book.id = add_book(book)



    author.add_book(book)

    add_book(book)

if __name__ == '__main__':
    db_init()
    main()