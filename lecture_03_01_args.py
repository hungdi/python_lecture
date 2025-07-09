

def introduce(name, age, *args, **kwargs):
    print(f"이름: {name}")
    print(f"나이: {age}")

    print("\n[추가설명(args)]")
    for arg in args:
        print(f"- {arg}")
    
    print("\n[기타 정보(kwargs)]")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


introduce(
    "Alice", 30,
    "개발자", "음악을 좋아함", # *args (개수 제한 없는 위치 기반 인자 목록)
    hobby="독서", country="Korea" # **kwargs (키워드 기반 인자목록, key=value형태이며, dict로 처리)
)

print('\n\n[인자가 없다면?]')
introduce(
    "Alice", 30
)

# dict를 배우고 난 다음에 진행하는게 좋지 않을까?

