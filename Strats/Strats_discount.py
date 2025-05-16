from abc import ABC, abstractmethod

class StratDiscount(ABC): #Strategy
    @abstractmethod
    def apply_discount(self, price):
        pass

class DiscountMember(StratDiscount):
    def apply_discount(self, price):
        return price * 0.9