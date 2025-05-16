from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.discount_strategy = None

    def set_StratDiscount(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def get_price_with_discount(self):
        if self.discount_strategy:
            return self.discount_strategy.apply_discount(self.price)
        return self.price

    @abstractmethod
    def show_info(self):
        pass
