from __future__ import annotations


class Book:
    def __init__(self, title: str, author: 'Author', price: float, description: str = '', isbn: str = ''):
        self.title = title
        self.price = price
        self.author = author
        self.description = description
        self.isbn = isbn

    def __str__(self):
        return f'{self.title} ({self.author.full_name})'
