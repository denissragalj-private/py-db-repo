
from __future__ import annotations



# Knjiga ima jednog autora, a autor može imati više knjiga
class Book:
    def __init__(self, title: str, author: 'Authors', price: float, isbn: str, description: str = ''):
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.isbn = isbn
    def __str__(self):
        return f'Naslov: {self.title}, ({self.author.full_name})'

