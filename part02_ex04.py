class AutoAttrMeta(type):
    def __init__(cls, name, bases, namespace):
        cls.created_by = "system"
        super().__init__(name, bases, namespace)
    

class MyModel(metaclass=AutoAttrMeta):
    pass

print(MyModel.created_by)