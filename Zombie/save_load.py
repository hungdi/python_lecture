import csv
from job import Civilian, Police, Doctor, Thief
from user import User, Status

def user_to_dict(user):
    return {
        "user_name": user.user_name,
        "job": user.job.job_name,
        "health": user.health,
        "food": user.food.amount,
        "antidote": user.antidote.amount,
        "infected": str(user.status.infected),  # csv는 문자열로 저장
        "infection_count": user.status.count,
        "alive": str(user.alive)  # csv는 문자열로 저장
    }

def user_from_dict(data):
    job_map = {"시민": Civilian, "경찰": Police, "의사": Doctor, "강도": Thief}
    job = job_map[data["job"]]()
    user = User(data["user_name"], job, health=float(data["health"]))
    user.food.amount = int(data["food"])
    user.antidote.amount = int(data["antidote"])
    user.status.infected = data["infected"].lower() == "true"
    user.status.count = int(data["infection_count"])
    user.alive = data["alive"].lower() == "true"
    return user

def save_users(users, filename="save.csv"):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        if users:  # 유저가 있을 때만 저장
            writer = csv.DictWriter(f, fieldnames=user_to_dict(users[0]).keys())
            writer.writeheader()
            writer.writerows(user_to_dict(u) for u in users)

def load_users(filename="save.csv"):
    try:
        with open(filename, "r", encoding="utf-8", newline='') as f:
            reader = csv.DictReader(f)
            return [user_from_dict(row) for row in reader]
    except FileNotFoundError:
        return []
