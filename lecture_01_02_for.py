list_a = [1, 3, 5, 7, 9]
list_b = [1, 2, 3, 5, 8]

for i in range(len(list_a)):
    for j in range(len(list_b)):
        if list_a[i] == list_b[j]:
            print(f'두 값이 같습니다.list_a[{i}]={list_a[i]},list_b[{j}]={list_b[j]}')


for item_a in list_a:
    for item_b in list_b:
        if item_a == item_b:
            print(f'두 값이 같습니다. item_a={item_a}, itemb={item_b}')


# 연습문제 2

n = int(input("정수입력:"))

for i in range(1, n):
    if i % 4 == 0:
        print(f'첫번째 4의 배수 등장:{i}')
        break

for i in range(1, n):
    if i % 3 == 0:
        continue
    else:
        print(i)


        



# 연습문제 3