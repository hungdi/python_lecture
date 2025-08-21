from typing import Protocol

# 1. Printable 프로토콜 정의
class Printable(Protocol):
    def print_content(self) -> str:
        ...

# 3. Book 클래스 구현 (Printable 프로토콜을 따름)
class Book:
    def __init__(self, title: str):
        self.title = title

    def print_content(self) -> str:
        return f"책 제목: '{self.title}'"

# 4. Document 클래스 구현 (Printable 프로토콜을 따름)
class Document:
    def __init__(self, name: str):
        self.name = name

    def print_content(self) -> str:
        return f"문서 이름: '{self.name}'"

# 5. print_item 함수 작성
def print_item(item: Printable) -> None:
    print(f"출력 내용: {item.print_content()}")

# --- 정답 코드 예시 ---

my_book = Book("파이썬 타입 힌트")
my_document = Document("중요 보고서")

print_item(my_book)      # '출력 내용: 책 제목: '파이썬 타입 힌트'' 출력
print_item(my_document)  # '출력 내용: 문서 이름: '중요 보고서'' 출력

# 프로토콜을 따르지 않는 객체는 타입 체커에서 에러 발생
# class MyCar:
#     def run(self):
#         return "running"
# my_car = MyCar()
# print_item(my_car)  # 타입 체커 에러