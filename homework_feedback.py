menu = {'아메리카노':3000, '카페라떼':4000, '레몬에이드':4500}
menu_count={}
total = 0
ordered_menu=set()

print(f'[카페메뉴판]')
print("".join([f"-{k}:{v}\n" for k,v in menu.items()]))

def count(order):
    if order in menu:
        menu_count[order] = menu_count.get(order,0) +1
        ordered_menu.add(order)
    elif order == "끝":
        return
    else:
        print(f'{order}는 없는 메뉴입니다.')

while True:
    order = input("메뉴를 입력하세요 (종료하려면 '끝'):")
    count(order)

    if order == "끝":
        break

for k,v in menu_count.items():
    price = menu[k]
    total += price * v

print(f'일매출:{total:,}원')

def count_max():
    best_menu = ""
    best_count = -1
    for k,v in menu_count.items():
        if v >= best_count:
            best_menu = k
            best_count = v
    return best_menu, best_count

print(f'{ordered_menu}')



best_menu, best_count = count_max()
print(f"오늘의 인기메뉴:{best_menu}")





# 실행시킬때 Work Flow
#1. 메뉴 목록 제공
#2. Input으로 주문할 메뉴 입력
#3. 누적 주문 갯수를 Count
#4. Count한 갯수와 매뉴Values를 매칭시켜서 *하여 총 매출을 구함
#5. 가장 많이 Count된 메뉴 1개를 오늘의 인기메뉴로 보여줌