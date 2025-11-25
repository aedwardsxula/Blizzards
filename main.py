from datetime import datetime, timedelta
from Blizzards.user_profile import Profile
from Blizzards.study_session import StudySession
from Blizzards.invite_logic import InviteLogic
from Blizzards.auto_cancel import AutoCancelJob
from Blizzards.flashcards import FlashcardGenerator

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



    #Testing User_profile class
    #Create 5 profiles and call their methods
    p1 = Profile("Sam", "CIS", "Physics", "Unknown")
    p1.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday":["11AM"]})
    
    p2 = Profile("Jamie", "Math", "CIS", "Unknown")
    p3 = Profile("Taylor", "Biology", "Chemistry", "Unknown")
    p4 = Profile("Jordan", "History", "English", "Unknown")
    p5 = Profile("Casey", "Art", "Design", "Unknown")
    profiles = [p1, p2, p3, p4, p5]
    for profile in profiles:
        if profile.major == "Art":
            profile.update_schedule({"Tuesday": ["1PM", "3PM"]})
        else:
            profile.update_schedule({"Friday": ["10AM"]})
        print(profile)
        print("Updated schedule:", profile.schedule)
        print("-" * 40)

    #Create and event to test AutoCancelJob
    e1 = Event("Math Exam", datetime.now() + timedelta(days=1))
    auto_cancel = AutoCancelJob(e1, 2)  # Auto-cancel if not confirmed in 1 hour
    print("\nAutoCancelJob created for event:", auto_cancel.event.name)
    



if __name__ == "__main__":
    main()