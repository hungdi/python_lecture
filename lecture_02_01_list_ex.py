

def calculate_total_cost(list):
    total_cost = 0
    for drink in list:
        total_cost += menu[drink]

    return total_cost

menu = {'아메리카노': 3000, '카페라떼': 4000, '레몬에이드':4500}



order_list = []
order_set = set()
for i in range(3):
    order = input('주문할 메뉴를 입력하세요:')
    if order in menu:
        order_list.append(order)
        order_set.add(order)
# 총금액 출력
cost = calculate_total_cost(order_list)
print('[결과]')
print(f'총 금액: {cost}원')
print(f'주문한 메뉴: {order_list}')
print(f'오늘의 인기 메뉴: {order_set}')



