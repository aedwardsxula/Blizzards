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

    def invite(self, invitee):
        print(f"Inviting {invitee} to study session on {self.topic}")

    def confirm(self):
        print(f"Confirming study session on {self.topic}")
        self.status = "confirmed"

    def cancel(self):
        print(f"Cancelling study session on {self.topic}")
        self.status = "cancelled"