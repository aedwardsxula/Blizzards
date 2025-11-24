#Implement AutoCancel Job (inherits from StudySession)
#Auto-cancels after X hours
#Notifies buddies of cancellation
from Blizzards.study_session import StudySession
class AutoCancelJob(StudySession):
    def __init__(self, proposer, time, place, topic, status="pending", cancel_after_hours=2):
        super().__init__(proposer, time, place, topic, status)
        self.cancel_after_hours = cancel_after_hours

    def auto_cancel(self):
        print(f"Auto-cancelling study session on {self.topic} after {self.cancel_after_hours} hours")
        self.cancel()
        self.notify_buddies()

    def notify_buddies(self):
        print(f"Notifying buddies of cancellation for study session on {self.topic}")