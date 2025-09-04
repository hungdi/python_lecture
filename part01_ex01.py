# part01_ex01.py
# 파이썬 딕셔너리를 이용한 해시 테이블 기능 구현
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        """데이터를 삽입합니다."""
        self.table[key] = value

    def search(self, key):
        """데이터를 검색합니다."""
        return self.table.get(key) # get() 메서드는 키가 없으면 None을 반환

    def delete(self, key):
        """데이터를 삭제합니다."""
        if key in self.table:
            del self.table[key]


my_hash_table = HashTable()

# 데이터 삽입
my_hash_table.insert("apple", 1000)
my_hash_table.insert("banana", 2000)
my_hash_table.insert("orange", 1500)
print(f"현재 테이블: {my_hash_table.table}")

# 데이터 검색
price_of_apple = my_hash_table.search("apple")
print(f"사과의 가격: {price_of_apple}원") # 1000원

# 없는 키 검색
price_of_grape = my_hash_table.search("grape")
print(f"포도의 가격: {price_of_grape}") # None

# 데이터 삭제
my_hash_table.delete("banana")
print(f"바나나 삭제 후 테이블: {my_hash_table.table}")