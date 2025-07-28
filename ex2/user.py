class User:
    def __init__(self, name):
        self.name = name
        self.borrow_books = []

    def can_borrow(self):
        if len(self.borrow_books) < 3:
            return True

    def borrow(self, book):
        if self.can_borrow():
            self.borrow_books.append(book)
            print(f"{self.name} 님이 {book.title}을 빌렸습니다.")
        else:
            print("대출 가능 권수 초과.")
    

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
    
    def can_borrow(self):
        return True
    
    
    