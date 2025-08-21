class Player:
    def __init__(self, name, hp, mp, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = level

player = Player("Archer", 120, 80, 5)

# 직렬화 대상 속성 가져오기 (메서드, 특수 속성 제외)
fields = [attr for attr in dir(player) 
          if not attr.startswith("_") and not callable(getattr(player, attr))]

# JSON 포맷 수동 생성
items = []
for field in fields:
    value = getattr(player, field)
    # 문자열은 따옴표 처리
    if isinstance(value, str):
        items.append(f'"{field}": "{value}"')
    else:
        items.append(f'"{field}": {value}')

json_data = "{\n  " + ",\n  ".join(items) + "\n}"
print(json_data)