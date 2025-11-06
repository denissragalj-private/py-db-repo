from models.authors import Author
from models.books import Book
from repositories.author_repos import add_author
from repositories.bd_init import db_init
from repositories.book_repos import add_book


def main():
    # Kreiraj autora
    first_name = input('Upiste ime autora: ')
    last_name = input('Upiste prezime autora: ')
    author = Author(first_name, last_name)
    author.id = add_author(author)
    # Kreiraj knjigu
    title = input('Upiste naziv knjige: ')
    description = input('Upiste kratki opis knjige: ')
    isbn = input('Upiste ISBN knjige: ')
    price = float(input('Upiste cijenu knjige: '))
    book = Book(title, author, price, description, isbn)
    book.id = add_book(book)
    # Povezi knjigu sa autorom
    author.add_book(book)

# Pokreni program
if __name__ == '__main__':
    db_init()
    main()
