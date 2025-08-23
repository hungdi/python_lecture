def atm_withdraw():
    
    balance = 100000

    while True:
        
        print(f"현재 잔액: {balance}")
        input_value = input("출금 금액 입력 (exit로 종료):")

        if input_value == 'exit':
            print('종료')
            break

        input_int_value = int(input_value)
        # 만원 단위만 허용
        if input_int_value % 10000 != 0:
            print("만원 단위만 가능")
            continue

        if input_int_value <= 0:
            print("올바른 금액이 아님")
            continue

        if input_int_value > balance:
            print("잔액 부족")
            continue

        balance = balance - input_int_value
        print(f"출금 완료, 잔액:{balance}")

    return balance


print(atm_withdraw())