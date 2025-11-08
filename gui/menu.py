from repositories.author_repos import add_author, get_author_by_name, update_author, delete_author
from repositories.book_repos import add_book
from models.authors import Author
from models.books import Book

def prikazi_menu():
    print("\nOdaberite opciju:")
    print("1. Dodaj autora i knjigu")
    print("2. Ažuriraj autora")
    print("3. Obriši autora")
    print("4. Izlaz")

def unos_autora_i_knjige():
    first_name = input("Upisite ime autora: ")
    last_name = input("Upisite prezime autora: ")
    author = Author(first_name, last_name)
    author.id = add_author(author)

    title = input("Upisite naziv knjige: ")
    description = input("Upisite kratki opis knjige: ")
    isbn = input("Upisite ISBN knjige: ")
    price = float(input("Upisite cijenu knjige: "))
    book = Book(title, author, price, description, isbn)
    book.id = add_book(book)

    author.add_book(book)
    print("Autor i knjiga su dodani.\n")

def meni():
    while True:
        prikazi_menu()
        izbor = input("Unesite opciju: ")
        if izbor == "1":
            unos_autora_i_knjige()
        elif izbor == "2":
            print("Opcija za ažuriranje autora tek treba biti implementirana.")
        elif izbor == "3":
            print("Opcija za brisanje autora tek treba biti implementirana.")
        elif izbor == "4":
            print("Kraj programa.")
            break
        else:
            print("Nepoznata opcija, pokušajte ponovo.")

if __name__ == "__main__":
    meni()
