from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator
from event import Event
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

def generate_study_sessions():
    profile1 = Profile(300123, "Alice", "Jones", "CS")
    profile2 = Profile(300456, "Bob", "Smith", "CIS")

    topics = [
        "Algorithms", "Data Structures", "Operating Systems", "Networks",
        "Databases", "Software Engineering", "Cybersecurity",
        "Machine Learning", "Artificial Intelligence", "Web Development"
    ]
    places = ["Library", "UC", "Online", "NCF", "Admin", "Xavier South"]
    base_time = datetime(2025, 11, 21, 10, 0)

    study_sessions = []
    for i in range(30):
        time = base_time + timedelta(days=random.randint(0, 10), hours=random.randint(0, 8))
        topic = random.choice(topics)
        place = random.choice(places)
        session = StudySession(f"User{i}", time, place, topic, "pending")
        study_sessions.append(session)

    for session in study_sessions[:10]:
        event = Event(session.topic, session.time)
        event.add_event(profile1)

    for session in study_sessions[10:20]:
        event = Event(session.topic, session.time)
        event.add_event(profile2)

    for session in study_sessions[20:]:
        session.invite(profile1, profile2)

    # Print schedules for verification
    print(f"\nProfile 1 Schedule ({profile1.first_name} {profile1.last_name}):")
    for e in profile1.schedule:
        print(f"- {e}")

    print(f"\nProfile 2 Schedule ({profile2.first_name} {profile2.last_name}):")
    for e in profile2.schedule:
        print(f"- {e}")

def main():
    print("Driver started")
    print_welcome_banner()



    #Testing User_profile class
    #Create 5 profiles and call their methods
    p1 = Profile(901, "Sam", "Jones", "CIS")
    # p1.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday":["11AM"]})
    
    p2 = Profile(902, "Jamie", "Williams", "CS")
    p3 = Profile(903, "Taylor", "Ibrahim", "CS")
    p4 = Profile(925, "Jordan", "Evans", "BINF")
    p5 = Profile(914, "Casey", "Nguyen", "CIS")
    profiles = [p1, p2, p3, p4, p5]
    for profile in profiles:
        if profile.major == "Art":
            profile.update_schedule({"Tuesday": ["1PM", "3PM"]})
        # else:
            # profile.update_schedule({"Friday": ["10AM"]})
        print(profile)
        print("Updated schedule:", profile.schedule)
        print("-" * 40)

    #Create and event to test AutoCancelJob
    e1 = Event("Math Exam", datetime.now() + timedelta(days=1))
    # auto_cancel = AutoCancelJob(e1, 2)  # Auto-cancel if not confirmed in 1 hour
    # print("\nAutoCancelJob created for event:", auto_cancel.event.name)
    
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

    profileA, profileB = random.sample(profiles, 2)
    chosen_session = random.choice(study_sessions)

    session1 = StudySession(proposer=profileA, time="3PM", place="Library", topic="Sorting Algorithms")
    session1.invite(profileA, profileB )

    print("\nDriver ended")






if __name__ == "__main__":
    main()
    generate_study_sessions()