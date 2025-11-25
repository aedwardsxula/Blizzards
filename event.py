#Create an Event class that has attributes: what (str) and when (DateTime). 
# Create a constructor and __str__ methods.
from datetime import datetime
class Event:
    def __init__(self, what: str, when: datetime):
        self.what = what
        self.when = when

    def __str__(self):
        return f"Event: {self.what} at {self.when.strftime('%m/%d/%Y at %I:%M %p')}"
    def __repr__(self):
        return self.__str__()