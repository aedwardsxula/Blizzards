#Implement StudySession Class
#Attributes: proposer, time, place, topic, status
#Methods: invite(), confirm(), cancel()
from datetime import datetime
import profile
class StudySession:
    def __init__(self, proposer, time, place, topic,reason = None ,status="pending"):
        if time is None or not isinstance(time, datetime):
            raise ValueError("Time must be provided")
        if not place or not isinstance(place, str):
            raise ValueError("Place must be provided")
        if reason is None:
            reason = topic
        if not reason or not isinstance(reason, str):
            raise ValueError("Reason must be provided")
        
        self.proposer = proposer
        self.time = time
        self.place = place
        self.topic = topic
        self.status = status
        self.reason = reason

    def __str__(self):
        time_str = self.time.strftime("%A, %b %d, %Y at %I:%M %p")
        return f"Study Session on {self.topic} proposed by {self.proposer} at {self.place} on {time_str}. Status: {self.status}"   

    def __repr__(self):
        return self.__str__() 

    @staticmethod
    def _datetime_in_profile(profile, dt: datetime):
        for entry in profile.schedule:
            if hasattr(entry, "when") and entry.when == dt:
                return True
            if hasattr(entry, "time") and entry.time == dt:
                return True
        return False
    
    def invite(self, profile_1, profile_2):
        # Example usage of _datetime_in_profile to avoid "not accessed" error
        if self._datetime_in_profile(profile_1, self.time) or self._datetime_in_profile(profile_2, self.time):
            print("One of the profiles is busy at this time.")
            return False
        
        profile_1.schedule.append(self)
        profile_2.schedule.append(self)
        print(f"Inviting {profile_1.name} to study session on {self.topic}")
        return True

    def confirm(self):
        print(f"Confirming study session on {self.topic}")
        self.status = "confirmed"

    def cancel(self):
        print(f"Cancelling study session on {self.topic}")
        self.status = "cancelled"
        
    def remove(self, profile_a, profile_b):
        in_a = self in profile_a.schedule
        in_b = self in profile_b.schedule

        if not (in_a and in_b):
            print("Remove aborted: session not present in both profiles.")
            return False

        profile_a.schedule.remove(self)
        profile_b.schedule.remove(self)
        print(f"Removed study session on '{self.reason}' from Profiles {profile_a.id} and {profile_b.id}")
        return True

