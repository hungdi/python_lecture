import json
from job import Civilian, Police, Doctor, Thief
from resource import Resource
from user import User, Status

def user_to_dict(user):
    return {
        "user_name": user.user_name,
        "job": user.job.job_name,
        "resource": vars(user.resource),
        "status": vars(user.status),
        "alive": user.alive
    }

def user_from_dict(data):
    job_map = {"시민": Civilian, "경찰": Police, "의사": Doctor, "강도": Thief}
    job = job_map[data["job"]]()
    resource = Resource(**data["resource"])
    status = Status(**data["status"])
    user = User(data["user_name"], job, resource, status)
    user.alive = data.get("alive", True)
    return user

def save_users(users, filename="save.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([user_to_dict(u) for u in users], f, ensure_ascii=False, indent=2)

def load_users(filename="save.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return [user_from_dict(u) for u in json.load(f)]
