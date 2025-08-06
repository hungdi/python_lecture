class Movable:
    def move(self, dx, dy):
        print(f"Move by ({dx}, {dy})")
    
class Drawable:
    def draw(self):
        print("Drawing character")


class Player(Movable, Drawable):
    pass

# Player에 그냥 move, draw함수를 구현해도 동작은 동일합니다
# 그러나 만약에 move, draw를 써야하는 캐릭터들이 많다면?
# 로직이 바뀌었을 때 모든 Player(다양한 플레이어 클래스가 있다고 가정)의 move, draw를 바꿔야한다면?
