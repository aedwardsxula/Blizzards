#Create an Event class that has attributes: what (str) and when (DateTime). 
# Create a constructor and __str__ methods.
from datetime import datetime
class Event:
    def __init__(self, what: str, when: datetime):
        self.what = what
        self.when = when

    def __str__(self):
        formatted_time = self.when.strftime("%m/%d/%Y at %I:%M %p")
        return f"Event: {self.what} at {formatted_time}"
    