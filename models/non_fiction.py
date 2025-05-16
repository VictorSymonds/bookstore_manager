from models.book import Book

class NonFiction(Book):
    def show_info(self):
        return f"Non-Fiction: {self.title} by {self.author} - ${self.price}"