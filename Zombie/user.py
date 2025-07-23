from resource import Resource

class Status:
    def __init__(self, infected=False, count=0):
        self.infected = infected
        self.count = count

class User:
    def __init__(self, user_name, job, resource: Resource, status: Status):
        self.user_name = user_name
        self.job = job
        self.resource = resource
        self.status = status
        self.alive = True
