class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
    def buy(self, vm, drink):
        if self.money >= drink.price:
            self.money -= drink.price
            vm.sell(drink)
            print(f"{drink.name}을 구매하셨습니다.")
        else:
            print(f"소지금이 부족해서 구매할 수 없습니다.")

