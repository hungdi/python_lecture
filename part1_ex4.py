class Animal:
    total_cnt = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.total_cnt += 1

    def introduce(self):
        print(f"안녕, 나는 {self.species}이고 이름은 {self.name}이야")
    
    @classmethod
    def get_total_count(cls):
        print(f"전체 동물의 수는 {cls.total_cnt}개 입니다.")

    @staticmethod
    def is_animal_name_valid(name):
        return name.isalpha() and len(name) >= 2


a1 = Animal("가을", "Dog")
a2 = Animal("초코", "Dog")
a1.introduce()

Animal.get_total_count()
print(Animal.is_animal_name_valid("abc")) # true
print(Animal.is_animal_name_valid("123")) # false