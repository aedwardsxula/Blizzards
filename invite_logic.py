#Implement InviteLogic Class (inherits from StudySession)
#Additional attribute: accept/decline
#Methods: accept_invite(), decline_invite()
from Blizzards.study_session import StudySession



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
        
    def check_duplicate_datetime(self, profile):
        for session in profile.schedule:
            if hasattr(session, "time") and session.time == self.time:
                return True
        return False

    def add_to_profile(self, profile):
        # Prevent duplicate datetimes
        if not self.check_duplicate_datetime(profile):
            profile.schedule.append(self)
            return True
        return False  # Duplicate prevented