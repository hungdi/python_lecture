from order import Order

class Kitchen:
    def __init__(self):
        self.order_list = []

    
    def receive_order(self, order):
        self.order_list.append(order)
        
    def cook_order(self):
        for order in self.order_list:
            # food_list를 조리시간순으로 정렬
            sorted_food = sorted(order.foods, key=lambda x:x.cooking_time)
            for food in sorted_food:
                print(f"{food.name}(조리시간:{food.cooking_time}분) 요리완료")
            print(f"{order.user.name}님의 주문이 모두 완료되었습니다.")