#Create an Event class that has attributes: what (str) and when (DateTime). 
# Create a constructor and __str__ methods.
from datetime import datetime
class Event:
    def __init__(self, what: str, when: datetime):
        self.what = what
        self.when = when

    def add_event(self, profile):
    # Reject exact duplicate event
        for event in profile.schedule:
            if event.what == self.what and event.when == self.when:
                print(f"Cannot add {self.what} for {profile.first_name} {profile.last_name}: Duplicate event.")
                return False

        # NEW: Reject any event with the same DATE + TIME
        for event in profile.schedule:
            # Handles Event.when AND StudySession.time
            existing_time = getattr(event, "when", getattr(event, "time", None))
            if existing_time == self.when:
                print(f"Cannot add event: Time conflict! {profile.first_name} already has something at this time.")
                return False

        # Safe to add
        profile.schedule.append(self)
        print(f"Added {self.what} to {profile.first_name} {profile.last_name}'s schedule.")
        return True

        
        


    def __str__(self):
        formatted_time = self.when.strftime("%m/%d/%Y at %I:%M %p")
        return f"Event: {self.what} at {formatted_time}"
    