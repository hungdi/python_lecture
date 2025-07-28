class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    
    def lend_book(self, user, book):
        for lib_book in self.books:
            if lib_book == book:
                # user borrow 처리
                user.borrow(book)
                # remove 처리
                self.books.remove(book)
                return
        print("그런 도서는 없습니다.")

    
