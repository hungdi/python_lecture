class MetaRequireFields(type):
    def __new__(metacls, name, bases, namespace):
        required = ['version', 'author']
        for key in required:
            if key not in namespace:
                raise TypeError(f"{name} 클래스에 '{key}' 속성이 필요합니다.")
        
        return super().__new__(metacls, name, bases, namespace)
    
class GoodClass(metaclass=MetaRequireFields):
    version = "1.0"
    author = "uncia"

# 이 클래스는 에러발생!
class BadClass(metaclass=MetaRequireFields):
    version = "1.0"

goodone = GoodClass()
badone = BadClass()