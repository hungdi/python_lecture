data = ["  Tom  ", "  Alice ", " Bob"]

# 데이터 전처리: 양쪽 공백 제거 + 소문자 변환
def clean_data(data_list, transform_func):
    return [transform_func(item) for item in data_list]

# 고차 함수 + 람다 사용
cleaned = clean_data(data, lambda x: x.strip().lower())

print(cleaned)  # ['tom', 'alice', 'bob']