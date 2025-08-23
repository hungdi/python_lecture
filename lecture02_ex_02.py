import random
def guess_number():
    x = random.randint(1, 50)
    try_num = 0
    while try_num < 7:
        n = input("숫자를 입력하세요.:")
        if n == 'q':
            break
        if not n.isdigit():
            print("정수를 입력하세요.")
            continue
        if int(n) < x:
            print("더 큰 수")
        elif int(n) > x:
            print("더 작은 수")
        else:
            print("정답")
            return
        try_num += 1
    else:
        print("실패")


guess_number()



