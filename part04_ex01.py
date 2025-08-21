class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, attr_name):
        print(f"{attr_name} 속성을 찾고있습니다.")
        return super().__getattribute__(attr_name)
    
    def __getattr__(self, attr_name):
        # 'attr_name'은 사용자가 접근하려 한 속성 이름입니다.
        print(f"'{attr_name}' 속성을 찾을 수 없습니다. 기본값을 반환합니다.")
        return "속성 없음"

student = Student("hong", 36)

print(student.name)
print(student.age)
print(student.major)

