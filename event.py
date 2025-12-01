#Create an Event class that has attributes: what (str) and when (DateTime). 
# Create a constructor and __str__ methods.
from datetime import datetime
class Event:
    def __init__(self, what: str, when: datetime):
        self.what = what
        self.when = when

    def add_event(self, profile):
        if self in profile.schedule:
            return False
        for event in profile.schedule:
            if event.what == self.what and event.when == self.when:
                print(f"Cannot add {self.what} for {profile.first_name} {profile.last_name}: Conflict or duplicate event.")
                return False
        profile.schedule.append(self)
        print(f"Added {self.what} to {profile.first_name} {profile.last_name}'s schedule.")
        return True
        
        


    def __str__(self):
        return f"Event: {self.what} at {self.when.strftime('%m/%d/%Y at %I:%M %p')}"
    def __repr__(self):
        return self.__str__()