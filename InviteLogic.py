#Implement InviteLogic Class (inherits from StudySession)
#Additional attribute: accept/decline
#Methods: accept_invite(), decline_invite()
from StudySession import StudySession


class InviteLogic(StudySession):
    def __init__(self, proposer, time, place, topic, status="pending", accepted=False):
        super().__init__(proposer, time, place, topic, status)
        self.accepted = accepted

    def accept_invite(self):
        self.accepted = True
        print(f"Invite accepted by {self.proposer}")

    def decline_invite(self):
        self.accepted = False
        print(f"Invite declined by {self.proposer}")