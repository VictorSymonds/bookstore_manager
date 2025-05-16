class BookManager:
    def __init__(self):
        self.books = []
        self.observers = []

    def add_book(self, book):
        self.books.append(book)
        self.notify_observers(book)
    
    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, book):
        for observer in self.observers:
            observer.update(book)

class BookObserver:
    def update(self, book):
        print(f"New book has been added: {book.title} by {book.author}")