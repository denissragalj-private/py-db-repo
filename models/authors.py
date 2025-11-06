
from __future__ import annotations



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

    def add_book(self, book: 'Book'):
        self.books.append(book)
    
