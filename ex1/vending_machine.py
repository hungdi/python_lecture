class VendingMachine:
    CHARGE_STOCK_BASIC_VALUE = 10
    def __init__(self, drinks):
        self.drinks = drinks
        self.valance = 0

    def add_drink(self, drink, count):
        self.drinks[drink] = self.drinks.get(drink, 0) + count

    """재고 충전을 위한 함수"""
    def charge_stock(self):
        for drink, count in self.drinks.items():
            self.drinks[drink] = self.drinks.get(drink, 0) + self.CHARGE_STOCK_BASIC_VALUE

    """drink 수량감소, 잔고 금액 관리"""
    def sell(self, drink):
        if self.drinks.get(drink, 0) == 0:
            print(f"{drink.name}은 현재 구매할 수 없습니다.")
            return
        self.drinks[drink] = self.drinks.get(drink, 0) - 1
        self.valance += drink.price


    """모든 메뉴 보기"""
    def show_menu(self):
        for drink, count in self.drinks.items():
            print(f"{drink.name}: {drink.price} 원 / 현재재고: {count}")
    
