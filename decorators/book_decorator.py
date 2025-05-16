from models.book import Book

class SignedBook(Book): #Decorator
    def __init__(self, book: Book):
        self._book = book

    def show_info(self):
        return self._book.show_info() + " (signed)"

    def get_price_with_discount(self):
        original_price = self._book.get_price_with_discount()
        return original_price + 5.0

    def set_StratDiscount(self, strategy):
        self._book.set_StratDiscount(strategy)

    def __getattr__(self, name):
        return getattr(self._book, name)
