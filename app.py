from gui.menu import meni
from models.authors import Author
from models.books import Book
from repositories.author_repos import add_author
from repositories.bd_init import db_init
from repositories.book_repos import add_book



if __name__ == '__main__':
    db_init()
    meni()
