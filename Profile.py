# Implement Profile Class
#Attributes: name, major, minor, schedule
#Methods: update_schedule()

class Profile:
    def __init__(self, name, major, minor, schedule=None):
        self.name = name
        self.major = major
        self.minor = minor
        self.schedule = schedule if schedule is not None else []

    def update_schedule(self, new_schedule):
        self.schedule = new_schedule