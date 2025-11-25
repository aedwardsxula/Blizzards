#Implement StudySession Class
#Attributes: proposer, time, place, topic, status
#Methods: invite(), confirm(), cancel()

class StudySession:
    def __init__(self, proposer, time, place, topic, status="pending"):
        self.proposer = proposer
        self.time = time
        self.place = place
        self.topic = topic
        self.status = status

    def invite(self, profile1, profile2):
        times_in_profile1 = any(session.time == self.time for session in profile1.schedule)
        times_in_profile2 = any(session.time == self.time for session in profile2.schedule)
        if not (times_in_profile1 and times_in_profile2):
            profile1.update_schedule(self)
            profile2.update_schedule(self)
            print(f"Invited {profile1.first_name} and {profile2.first_name} to study session on {self.topic} at {self.time}")
        else:
            print("Cannot invite: Time conflict in both profiles' schedules.")

    def confirm(self):
        print(f"Confirming study session on {self.topic}")
        self.status = "confirmed"

    def cancel(self):
        print(f"Cancelling study session on {self.topic}")
        self.status = "cancelled"