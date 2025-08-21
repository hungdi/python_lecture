from typing import TypeVar, List

# 1. ItemType 이라는 타입 변수 정의
ItemType = TypeVar('ItemType')

# 2. get_item_at_index 제네릭 함수 작성
def get_item_at_index(data: List[ItemType], index: int) -> ItemType:
    """
    제네릭 함수: 리스트에서 특정 인덱스의 요소를 반환합니다.
    """
    return data[index]


# --- 정답 코드 예시 ---

# 정수 리스트 테스트
numbers = [10, 20, 30, 40, 50]
first_number = get_item_at_index(numbers, 0)
print(f"첫 번째 요소의 타입: {type(first_number)}, 값: {first_number}")

third_number = get_item_at_index(numbers, 2)
print(f"세 번째 요소의 타입: {type(third_number)}, 값: {third_number}")

# 문자열 리스트 테스트
names = ["Alice", "Bob", "Charlie"]
last_name = get_item_at_index(names, 2)
print(f"마지막 이름의 타입: {type(last_name)}, 값: {last_name}")

# 예외 처리 테스트 (주석을 해제하고 실행해보세요)
invalid_index_item = get_item_at_index(names, 3)
print(invalid_index_item)