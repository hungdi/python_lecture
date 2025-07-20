class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, rate):
        self.price = int(self.price * (1 - rate))

    def show_info(self):
        print(f"{self.name} - {self.price}원")

# 음식 객체 생성
pizza = Food("페퍼로니 피자", 15000)
burger = Food("치즈버거", 7000)

pizza.apply_discount(0.1)
pizza.show_info()
burger.show_info()