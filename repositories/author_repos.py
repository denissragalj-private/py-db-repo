import sqlite3

from constants import DB_PATH
from models.authors import Author

sql_create_author = '''
INSERT INTO author (first_name, last_name)
VALUES (?, ?)
'''

# pdohvati autora prema imenu i prezimenu
sql_get_author_by_name = '''
SELECT * FROM author
WHERE first_name LIKE ?
AND last_name LIKE ?   
'''


def get_author_by_name(first_name: str, last_name: str) -> Author | None:    # funkcija za dohvat autora prema imenu i prezimenu koja vraca objekt Author ili None
    try:                                                                        # pokušaj dohvatiti autora iz baze  
        with sqlite3.connect(DB_PATH) as conn:                                      # uspostavljanje veze s bazom podataka i otvaranje konteksta te na kraju automatsko zatvaranje veze i commit.
            cursor = conn.cursor()                                                      # kreiranje kursora za rad s bazom
            cursor.execute(sql_get_author_by_name, (first_name, last_name))             # izvrsavanje SQL upita za dohvat autora prema imenu i prezimenu i vračanje samo prvog rezultata (ako postoji)
            row = cursor.fetchone()                                                     # dohvat prvog reda rezultata upita
            if row:                                                                     # ako postoji red u kojem je pronaden autor u bazi
                author = Author(row[1], row[2])                                             # kreiraj objekt Author iz dohvaćenog reda koristeći indekse stupaca 1 i 2 (first_name, last_name)
                author.id = row[0]                                                          # postavi ID autora iz stupca 0
                return author                                                           # vrati objekt Author IZ baze
            return None                                                                 # ako autor nije pronaden, vrati None
    except Exception as ex:                                                         # hvatanje gresaka prilikom dohvata autora iz baze
        print(f"Dogodila se greska {ex}.")                                              # ispis greske ako do nje dodje
        return None                                                                     # vrati None ako dodje do greske                                           


def add_author(author: Author) -> int | None:                               # dodavanje autora u bazu podataka nova funkcija koja prima objekt Author i vraca njegov ID ili None
    if not isinstance(author, Author):                                          # AKO author NIJE objekt Author iz models.authors tj iz baze
        return None                                                                  # vrati None
    existing_author = get_author_by_name(author.first_name, author.last_name)   # nakon toga, provjeri da li autor vec postoji u bazi koristici funkciju 'get_author_by_name'
    if existing_author:                                                         # ako autor vec postoji, 
        return existing_author.id                                                    # vrati njegov ID iz baze
    try:                                                                        # pokušaj  dohvata ID-a novododanog autora iz baze
        with sqlite3.connect(DB_PATH) as conn:                                      # dodavanje novog autora u bazu
            cursor = conn.cursor()                                                      # kreiranje kursora za rad s bazom
            cursor.execute(sql_create_author, (author.first_name, author.last_name))    # izvrsavanje SQL upita za dodavanje autora
            return cursor.lastrowid                                                     # vracanje ID-a novododanog autora i cijelog kursora te zapisi promjene u bazu uz commit koji se izvrsava automatski uz with
    except Exception as ex:                                                     # hvatanje gresaka ako se ne uspije dodati autor u bazi
        print(f"Dogodila se greska {ex}.")                                          # ispis greske  ako do nje dodje
        return None                                                                 # vracanje None na mjeto ID-a ako dodje do greske nakon čega se u bazu nece spremiti novi autor.
