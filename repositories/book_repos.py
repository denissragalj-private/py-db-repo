from __future__ import annotations
import sqlite3

from constants import DB_PATH


sql_create_book = '''
INSERT INTO book (title, description, isbn, price, author_id)
VALUES (?, ?, ?, ?, ?)
'''


def add_book(book: 'Book') -> int:
    if isinstance(book, 'Book'):
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
