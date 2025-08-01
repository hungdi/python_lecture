class Parent:
    def greet(self):
        return "Hello"
    
class Child(Parent):
    def greet(self): # 부모 메서드 오버라이딩
        return "Hi!"
    

print(Child().greet()) # Hi! 출력
