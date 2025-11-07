import sqlite3

from constants import DB_PATH
from models.books import Book


sql_create_book = """
INSERT INTO book (title, description, isbn, price, author_id)
VALUES (?, ?, ?, ?, ?)
"""


def add_book(book: Book) -> int:
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
        print(f"Dogodila se greska {ex}.")


def get_book(id: int) -> Book:
    # 1. dohvati knjigu iz baze po id-u
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return Book(*row)
            return None
    except Exception as ex:
        print(f"Dogodila se greska {ex}.")


def delete_book(id: int):
    pass
    # 1. dohvati knjigu iz baze po id-u
    # 2. ako knjiga postoji, obrisati je iz baze
