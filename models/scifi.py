from models.book import Book

class Scifi(Book):
    def show_info(self):
        return f"Science Fiction: {self.title} by {self.author} - ${self.price}"