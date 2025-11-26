from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator

import random

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

def remove_two_sessions(session, profileA, profileB):
    removed = session.remove(profileA, profileB)
    if removed:
        print(f"Removed session on {session.topic} from one or both profiles' schedules.")
    else:
        print("Session not found in either profile's schedule.")

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
    
    # Create 33 study sessions
    sessions = []
    times = [datetime.now() + timedelta(days=i, hours=j) for i in range(1, 10) for j in range(9, 18)]
    topics = ["Calculus", "Calculus II", "Info Systems",  "Data Structures", "Chemistry"]
    places = ["Library", "Cafeteria", "Admin", "Zoom"]
    for i in range(33):
        session = StudySession(proposer=f"User{i}", time=random.choice(times), place=random.choice(places),topic=random.choice(topics), status="pending")
        sessions.append(session)
    for s in sessions:
        print(f"{s.proposer} scheduled {s.topic} at {s.place} ({s.time})")

    #remove sessions from two profiles
    for s in sessions:
        remove_two_sessions(s, p1, p2)

    #Create 222 study sessions
    study_sessions = []
    times = [datetime.now() + timedelta(days=i, hours=j) for i in range(1, 10) for j in range(9, 18)]
    topics = ["Calculus", "Calculus II", "Info Systems",  "Data Structures", "Chemistry"]
    places = ["Library", "Cafeteria", "Admin", "Zoom"]
    for i in range(33):
        s_session = StudySession(proposer=f"User{i}", time=random.choice(times), place=random.choice(places),topic=random.choice(topics), status="pending")
        study_sessions.append(s_session)
    for s in study_sessions:
        print(f"{s.proposer} scheduled {s.topic} at {s.place} ({s.time})")







if __name__ == "__main__":
    main()