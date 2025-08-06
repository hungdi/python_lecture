class MyMeta(type):
    def __new__(metacls, name, bases, namespace):
        print("1. 메타클래스:", metacls)
        print("2. 클래스 이름:", name)
        print("3. 부모 클래스들:", bases)
        print("4. 클래스 멤버들:", namespace)
        return super().__new__(metacls, name, bases, namespace)
    

class MyClass(metaclass=MyMeta):
    x = 10
    @classmethod
    def class_method(cls):
        return "나는 클래스 메서드"
    @staticmethod
    def static_method():
        return "나는 정적 메서드"
    
MyClass()
