from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator
from event import Event

# profiles
def mmp_driver():
    p1 = Profile(0, "Sam", "Maxey", "CS")
    p2 = Profile(1, "Jamie", "Johnson", "CE")
    p3 = Profile(2, "Taylor", "Jackson", "BINF")
    p4 = Profile(3, "Jordan", "Michael", "CIS")
    p5 = Profile(4, "Casey", "Brown", "CIS")        
    profiles = [p1, p2, p3, p4, p5]

    for profile in profiles:
        if profile.major == "CIS":
            profile.add_event(Event("Team Meeting", datetime(2025, 1, 7, 13, 0)))
            profile.add_event(Event("Office Hours", datetime(2025, 1, 7, 15, 0)))
        else:
            profile.add_event(Event("General Meeting", datetime(2025, 1, 10, 10, 0)))

        print(profile)
        print("Updated schedule:")
        for e in profile.schedule:
            print("   -", e)
        print("-" * 40)

if __name__ == "__main__":
    mmp_driver()
