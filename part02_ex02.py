def outer():
    def inner():
        print("이 함수는 outer 안에서만 쓰임")
    inner()

outer()