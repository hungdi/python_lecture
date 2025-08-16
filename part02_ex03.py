def outer(message_outer):
    message = message_outer

    def inner():
        print(f"내부함수에서 외부함수의 변수사용:{message}")
    
    inner()

outer("zz")