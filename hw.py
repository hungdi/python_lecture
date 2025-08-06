import random

class Resource:
    def __init__(self):
        self.food = 0
        self.antidote = 0

    def add_food(self): self.food += 1
    def add_antidote(self): self.antidote += 1

    def __str__(self):
        return f"식량:{self.food}, 해독제:{self.antidote}"


class JobMeta(type):
    # 필수속성 : job_name, base_hp, daily_hp_loss, resource_prob
    # 잘못된 직업 정의 시 예외 발생 () : raise TypeError(f"{name} 클래스는 '{attr}' 속성을 반드시 정의해야 합니다.")
    required_attr = ['job_name', 'base_hp', 'daily_hp_loss', 'resource_prob']
    def __new__(cls, name, bases, dct):
        if name != "Job":
            for attr in cls.required_attr:
                if attr not in dct:
                    raise TypeError(f"{name} class는 '{attr}' 속성을 반드시 정의해야합니다.")
        return super().__new__(cls, name, bases, dct)

class Job(metaclass=JobMeta):
    job_name = '기본직업'
    base_hp = 100
    daily_hp_loss = 5

    def __init__(self):
        self.resource_prob = {}

class GatherFoodAction:
    def gather_food(self, user):
        prob = type(self).resource_prob["food"]
        #print(f"GatherFoodAction {user.name} prob:{prob}")
        if random.random() < prob:
            user.resource.add_food()
            print(f"[{user.name}] 식량을 채집했습니다.")

class GatherAntidoteAction:
    def gather_antidote(self, user):
        prob = getattr(self, "resource_prob", {}).get("antidote", 0.0)
        if random.random() < prob:
            user.resource.add_antidote()
            print(f"[{user.name}] 해독제를 얻었습니다.")

class HealSelfAction:
    def heal_self(self, user):
        if user.hp < 60:
            user.hp += 10
            print(f"[{user.name}] 자가치유로 체력을 회복하였습니다.")

class StealAction:
    def steal(self, user, all_users):
        targets = [u for u in all_users if u!=user]
        target = random.choice(targets)
        if target.resource.food > 0 and random.random() < 0.5:
            target.resource.food -= 1
            user.resource.food += 1
            print(f"[{user.name}]이(가) {target.name}에게서 식량을 훔쳤습니다.")
        else:
            print(f"[{user.name}]의 도둑질이 실패했습니다.")

class FightAction:
    def fight(self, user, all_users):
        if random.random() < 0.4:
            target = random.choice([u for u in all_users if u != user])
            if target.resource.food > 0:
                target.resource.food -= 1
                user.resource.food += 1
                target.hp -= 10
                user.hp -=10
                print(f"[{user.name}]이(가) {target.name}과 싸워 식량을 빼앗았습니다. (상호체력 감소 -10)")


class Citizen(Job, GatherFoodAction, FightAction):
    # 클래스 변수들의 정의
    # job_name, base_hp, daily_hp_loss, resource_prob = { "food": x.x, "antidote": x.x }
    job_name = "시민"
    base_hp = 100
    daily_hp_loss = 10
    resource_prob = {
        "food": 0.6,
        "antidote": 0.1
    }

class Doctor(Job, GatherFoodAction, HealSelfAction):
    # 클래스 변수들의 정의
    # job_name, base_hp, daily_hp_loss, resource_prob = { "food": x.x, "antidote": x.x }
    job_name = "의사"
    base_hp = 100
    daily_hp_loss = 10
    resource_prob = {
        "food": 0.4,
        "antidote": 0.3
    }

class Police(Job, GatherFoodAction, FightAction):
    # 클래스 변수들의 정의
    # job_name, base_hp, daily_hp_loss, resource_prob = { "food": x.x, "antidote": x.x }
    job_name = "경찰"
    base_hp = 110
    daily_hp_loss = 10
    resource_prob = {
        "food": 0.7,
        "antidote": 0.1
    }


class Thief(Job, StealAction, FightAction):
    # 클래스 변수들의 정의
    # job_name, base_hp, daily_hp_loss, resource_prob = { "food": x.x, "antidote": x.x }
    job_name = "도둑"
    base_hp = 100
    daily_hp_loss = 10
    resource_prob = {
        "food": 0.0,
        "antidote": 0.3
    }


class User:
    def __init__(self, name, job_cls):
        self.name = name
        self.job = job_cls()
        self.hp = self.job.base_hp
        self.resource = Resource()

    def status(self):
        return f"[{self.name}] 직업: {self.job.job_name}, HP:{self.hp}, 자원:{self.resource}"
    
class Simulator:
    def __init__(self, users):
        self.users = users
        self.day = 0
    
    def run_day(self):
        self.day += 1
        for user in self.users:
            self.simulate_day(user)
        for user in self.users:
            print(user.status())
    
    def simulate_day(self, user):
        user.hp -= user.job.daily_hp_loss

        # 함수의 명세(이름과 매개변수)가 제각각이므로 문자열로 저장
        actions = [ 
            ("gather_food", 1),
            ("gather_antidote", 1),
            ("heal_self", 1),
            ("steal", 2),
            ("fight", 2),
        ]
        
        for method_name, arg_count in actions:
            method = getattr(user.job, method_name, None) # 함수의 이름가지고 함수 그 자체를 가져옴. 아래 코드와 유사함! 
            # 괄호를 붙이면 함수의 실행이며, 괄호를 안붇이는 경우 함수 그 자체를 받아오는것 (함수를 매개변수로!)
            #if method_name == "gather_food":
            #    method = user.job.gather_food
            #elif method_name == "fight":
            #    method = user.job.fight
            if callable(method): # 진짜 함수인지 확인하는 용도
                if arg_count == 1:
                    method(user)
                elif arg_count == 2:
                    method(user, self.users)

if __name__ == "__main__":
    users = [
        User("시민1", Citizen),
        User("의사1", Doctor),
        User("경찰1", Police),
        User("도둑1", Thief),
    ]

    simulator = Simulator(users)
    for _ in range(10):
        simulator.run_day()


