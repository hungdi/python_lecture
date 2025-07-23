import random
from job import Civilian, Police, Doctor, Thief
from user import User, Status

class UserSpawner:
    def __init__(self, birth_prob=0.2):
        self.birth_prob = birth_prob

    def spawn_if_needed(self, users):
        if random.random() < self.birth_prob:
            new_user = self.create_random_user()
            users.append(new_user)
            print(f"🎉 새로운 생존자 등장: {new_user.user_name} ({new_user.job.job_name})")

    def create_random_user(self):
        job_cls = random.choice([Civilian, Police, Doctor, Thief])
        job = job_cls()
        name = f"신규_{random.randint(1000, 9999)}"
        user = User(name, job, health=job.basic_hp)
        user.food.give()
        return user
