menu = {
    "아메리카노": 3000,
    "레몬에이드": 4000,
    "카페라떼": 5000,
}

orders = []
popular_menu = set() # 중복이 없어야돼서

def add_order(item):
    if item in menu:
        orders.append(item)
        popular_menu.add(item)
    else:
        print(f"{item}은 없는 메뉴입니다")
    

# 주문내역, 주문금액 출력
def show_order_summary():
    total = 0
    for item in orders:
        total += menu[item]
        print(f"주문내역:{item}")
    
    print(f"총금액:{total}")


# 인기메뉴 출력
def show_popular_menu():
    print("오늘의 인기 메뉴")
    for item in popular_menu:
        print(item)
    pass


# 주문 예시
add_order("아메리카노")
add_order("레몬에이드")
add_order("콜라")  # 없는 메뉴
add_order("카페라떼")
add_order("아메리카노")  # 인기 메뉴에는 중복으로 안 들어감

# 결과 출력
show_order_summary()
show_popular_menu()