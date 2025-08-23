pw = 3584
max_try_num = 3

def login_with_pin():
    for i in range(3):
        n = input("비밀번호를 입력하세요.:")
        if n == 'exit':
            print("프로그램 종료")
            return
        if int(n) == pw:
            print("로그인 성공!")
            return
        
        print(f"남은 횟수({max_try_num - (i+1)})")
    print("로그인 실패")


login_with_pin()

        

