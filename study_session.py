#Implement StudySession Class
#Attributes: proposer, time, place, topic, status
#Methods: invite(), confirm(), cancel()
from datetime import datetime
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

    def invite(self, invitee):
        print(f"Inviting {invitee} to study session on {self.topic}")

    def confirm(self):
        print(f"Confirming study session on {self.topic}")
        self.status = "confirmed"

    def cancel(self):
        print(f"Cancelling study session on {self.topic}")
        self.status = "cancelled"
        
    def remove(self, profileA, profileB):
        removed = False

        # Remove from profile A
        if self in profileA.schedule:
            profileA.schedule.remove(self)
            removed = True

        # Remove from profile B
        if self in profileB.schedule:
            profileB.schedule.remove(self)
            removed = True

        return removed