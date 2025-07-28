
from book import Book
from library import Library
from user import User, AdminUser


library = Library()
b1 = Book("퇴마록", "이우혁")
b2 = Book("건축무한육면각체의비밀", "장용민")
b3 = Book("깊은 강", "엔도슈샤쿠")
library.add_book(b1)
library.add_book(b1)
library.add_book(b1)
library.add_book(b2)
library.add_book(b2)
library.add_book(b2)
library.add_book(b3)
library.add_book(b3)
library.add_book(b3)

user = User("방문자1")
library.lend_book(user, b1)
library.lend_book(user, b1)
library.lend_book(user, b1)
library.lend_book(user, b1)


admin_user = AdminUser("관리자")
library.lend_book(admin_user, b2)
library.lend_book(admin_user, b2)
library.lend_book(admin_user, b2)
library.lend_book(admin_user, b2)
library.lend_book(admin_user, b3)
