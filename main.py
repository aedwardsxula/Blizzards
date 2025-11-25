from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator
from event import Event

def print_welcome_banner():
    banner = r"""
    ================================================
    __        __   _                            _         
    \ \      / /__| | ___ ___  _ __ ___   ___  | |   
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |_|   
      \ V  V /  __/ | (_| (_) | | | | | |  __/  _ 
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_|

    ________________________________________________
    
    Welcome to Study Buddies — let us learn together!
    ________________________________________________
    ================================================
    """
    print(banner)

def main():
    print (print_welcome_banner())



  

# profiles
    p1 = Profile(0, "Sam", "Maxey", "CS")
    p2 = Profile(1, "Jamie", "Johnson", "CE")
    p3 = Profile(2, "Taylor", "Jackson", "BINF")
    p4 = Profile(3, "Jordan", "Michael", "CIS")
    p5 = Profile(4, "Casey", "Brown", "CIS")        
    profiles = [p1, p2, p3, p4, p5]

    for profile in profiles:
        if profile.major == "CIS":
            profile.update_schedule(Event("Team Meeting", datetime(2025, 1, 7, 13, 0)))
            profile.update_schedule(Event("Office Hours", datetime(2025, 1, 7, 15, 0)))
        else:
            profile.update_schedule(Event("General Meeting", datetime(2025, 1, 10, 10, 0)))

        print(profile)
        print("Updated schedule:")
        for e in profile.schedule:
            print("   -", e)
        print("-" * 40)





if __name__ == "__main__":
    main()