
from collections import Counter

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        return isinstance(other, MenuItem) and self.name == other.name

    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return f"{self.name}: {self.price}원"

    def __repr__(self):  # 리스트에 포함된 상태로 출력할 때 사용됨
        return self.__str__()
    
class Menu:
    def __init__(self):
        self.item_list = []

    def add_item(self, item: MenuItem):
        self.item_list.append(item)

    def print_all(self):
        print(f"[메뉴판]")
        for item in self.item_list:
            print(f"{item.name}: {item.price}원")

    def get_menu_item(self, name):
        for item in self.item_list:
            if item.name == name:
                return item
        return None
    
    # 저렴한 메뉴 필터링
    def show_cheap_menus(self, max_price=4000):
        print(f"\n[{max_price}원 이하 저렴한 메뉴 보기]")
        # 조건에 맞는 메뉴만 필터링
        cheap_menu = list(filter(lambda item:item.price <= max_price, self.item_list))
        print(cheap_menu)

class Customer:
    def __init__(self, name, grade="NORMAL"):
        self.name = name
        self.grade = grade


class CustomerOrder:
    def __init__(self): #, customer: Customer, item: MenuItem):
        self.customer_order = {}

    def make_order(self, customer: Customer, item: MenuItem):
        self.customer_order.setdefault(customer, []).append(item)

    def get_customer_orders(self, customer):
        return self.customer_order.get(customer, None)
    
    def print_all(self):
        print("[주문목록]")
        for key,value in self.customer_order.items():
            line = ", ".join([v.name for v in value])
            print(f"{key.name}: {line}")

class StatisticsManager:
    def __init__(self, orders: CustomerOrder):
        self.orders = orders
    
    def show_popular_menu(self):
        print("\n[인기 메뉴 순위(Top 3)]")
        # MenuItem 별로 count

        all_items = []
        for item_list in self.orders.customer_order.values():
            all_items.extend(item_list)

        # print(all_items)

        counter = Counter(all_items)
        for menu, count in counter.most_common()[:3]:
            print(f"{menu.name}: {count}회")
        



if __name__ == "__main__":
    menu = Menu()
    menu.add_item(MenuItem("아메리카노", 3000))
    menu.add_item(MenuItem("카페라떼", 4000))
    menu.add_item(MenuItem("레몬에이드", 4500))
    menu.add_item(MenuItem("물", 1000))
    menu.add_item(MenuItem("콜라", 2000))
    menu.print_all()

    customer1 = Customer("김아무개", grade="VIP")
    customer2 = Customer("홍길동")
    customer3 = Customer("GUEST")

    orders = CustomerOrder()
    orders.make_order(customer1, menu.get_menu_item("아메리카노"))
    orders.make_order(customer1, menu.get_menu_item("레몬에이드"))
    orders.make_order(customer1, menu.get_menu_item("콜라"))
    orders.make_order(customer2, menu.get_menu_item("아메리카노"))
    orders.make_order(customer3, menu.get_menu_item("아메리카노"))
    orders.print_all()

    s = StatisticsManager(orders)
    s.show_popular_menu()
    menu.show_cheap_menus()

