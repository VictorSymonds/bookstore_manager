from factory_method.book_factory import BookFactory
from decorators.book_decorator import SignedBook
from Strats.Strats_discount import DiscountMember
from Observers.book_manager import BookManager
from Observers.book_manager import BookObserver

def main():

    manage = BookManager()
    user = BookObserver()
    manage.register_observer(user)

    book1 = BookFactory.create_book("Science Fiction", "World War Z", "Max Brooks", 16.99)
    book2 = BookFactory.create_book("Non-Fiction", "Sapiens", "Yuval Noah Harari", 18.99)
    book3 = BookFactory.create_book("Horror", "Night Shift", "Stephen King", 9.99)

    book1.set_StratDiscount(DiscountMember())
    book2.set_StratDiscount(DiscountMember())
    book3.set_StratDiscount(DiscountMember())

    book2 = SignedBook(book2)

    manage.add_book(book1)
    manage.add_book(book2)
    manage.add_book(book3)

    print("\n Information of books available in the store:")
    for book in manage.books:
        print(book.show_info())
        if isinstance(book, SignedBook):
            print(f"Price with signature: ${book.get_price_with_discount():.2f}")
        else:
            print(f"Price with discount: ${book.get_price_with_discount():.2f}")

if __name__ == "__main__":
        
    main()