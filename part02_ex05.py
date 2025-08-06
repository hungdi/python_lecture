class InstanceCounterMeta(type):
    def __init__(cls, name, bases, namespace):
        cls._instance_count = 0
        super().__init__(name, bases, namespace)
    
    def __call__(cls, *args, **kwargs):
        cls._instance_count += 1
        print(f"{cls.__name__} 인스턴스 생성횟수: {cls._instance_count}")
        return super().__call__(*args, **kwargs)
    

class User(metaclass=InstanceCounterMeta):
    def __init__(self, name):
        self.name = name


u1 = User("Alice")
u2 = User("Bob")
u3 = User("test")