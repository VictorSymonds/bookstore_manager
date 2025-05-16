from models.non_fiction import NonFiction
from models.scifi import Scifi
from models.horror import Horror

class BookFactory: #Factory Method
    @staticmethod
    def create_book(book_type, title, author, price):
        if book_type == "Science Fiction":
            return Scifi(title, author, price)
        elif book_type == "Non-Fiction":
            return NonFiction(title, author, price)
        elif book_type == "Horror":
            return Horror(title, author, price)
        else:
            raise ValueError(f"Unknown book type: {book_type}")