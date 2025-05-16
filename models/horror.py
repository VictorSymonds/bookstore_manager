from models.book import Book

class Horror(Book):
    def show_info(self):
        return f"Horror: {self.title} by {self.author} - ${self.price}"