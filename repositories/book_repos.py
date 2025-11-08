import sqlite3

from constants import DB_PATH
from models.books import Book


sql_create_book = '''
INSERT INTO book (title, description, isbn, price, author_id)
VALUES (?, ?, ?, ?, ?)
'''
sql_get_book = '''
SELECT * FROM book
WHERE id = ?
'''
sql_delete_book = '''
DELETE FROM book
WHERE id = ?
'''


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
        print(f'Dogodila se greska {ex}.')


def get_book(id) -> Book:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_get_book, (id,))
            book = cursor.fetchone()
            # medu korak dohvatiti autora iz baze i napraviti objekt Author
            # kada su svi podaci spremni napraviti objekt Book i vratiit ga pomocu return


    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def delete_book(id: int) -> str:
    # 1. dohvatiti knjigu iz baze koja ima dobiveni ID
    book_from_db = get_book(id)

    # 2. ako postoji knjiga u bazi izbrisi je i vrati poruku OK
    if book_from_db is not None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_delete_book, (id,))
                return 'OK'
        except Exception as ex:
            print(f'Dogodila se greska {ex}.')

    # ako ne postoji vratiti poruku da nema takve knjige u bazi
    else:
        return f'Ne postoji trazena knjiga u bazi!'


def update_book(book: Book) -> str:
    pass  # implementacija funkcije za ažuriranje knjige u bazi podataka još nije dovršena
    # 1. dohvatiti knjigu iz baze koja ima ID iz objekta book
    # 2. ako postoji knjiga u bazi, ažurirati njezine podatke s podacima iz objekta book i vratiti poruku OK
    # 3. ako ne postoji vratiti poruku "Knjiga s danim ID-om ne postoji."   

def get_all_books() -> list[Book]:
    pass  # implementacija funkcije za dohvat svih knjiga iz baze podataka još nije dovršena
    # 1. dohvatiti sve knjige iz baze
    # 2. za svaku knjigu dohvatiti i pripadajućeg autora iz baze
    # 3. kreirati objekte Book i Author te ih dodati u listu koja se na kraju vraća 
    # 4. vratiti listu objekata Book

