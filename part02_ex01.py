class MyMeta(type):
    # 생성될 때 어떻게 
    def __new__(cls, name, bases, dct):
        print(f"{name} 클래스를 만듭니다.")
        
        return super().__new__(cls, name, bases, dct)
    


class MyClass(metaclass=MyMeta):
    def __new__(cls):
        print(f"{cls}")
        return super().__new__(cls)
    pass

MyClass()