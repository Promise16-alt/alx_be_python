from book_class import Book
def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book
if__name__=="__main__":
    main()
