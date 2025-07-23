import os
import random
from job import Civilian, Police, Thief
from resource import Resource
from user import User, Status
from simulator import SurvivalSimulator
from interaction import InteractionManager
from user_spawner import UserSpawner
from save_load import save_users, load_users
from simulation_controller import SimulationController

def get_initial_users():
    return [
        User("강도1", Thief(), Resource(food=0, antidote=0, health=60), Status()),
        User("경찰1", Police(), Resource(food=2, antidote=1, health=100), Status()),
        User("시민1", Civilian(), Resource(food=3, antidote=0, health=100), Status()),
    ]

def simulate_from_file(filename="save.json", days=3):
    users = load_users(filename) if os.path.exists(filename) else get_initial_users()

    sim = SurvivalSimulator()
    inter = InteractionManager(users)
    spawner = UserSpawner(birth_prob=0.001)
    controller = SimulationController(sim, inter, spawner)

    for day in range(1, days + 1):
        controller.run_day(users, day)

    save_users(users, filename)
    print(f"\n[저장 완료] {filename}에 상태 저장됨")


if __name__ == '__main__':
    simulate_from_file(days=7)
