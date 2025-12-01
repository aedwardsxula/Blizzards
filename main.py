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
    print_welcome_banner()

    while True:
        print("\n==================== STUDY BUDDY APP ====================")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. List All Profiles")
        print("4. Change Major")
        print("5. Add Event")
        print("6. Remove Event")
        print("7. Sort Events")
        print("8. View Events")
        print("9. Create and Invite Study Session")
        print("10. Accept Invite")
        print("11. Decline Invite")
        print("12. Auto-Cancel Session")
        print("13. Remove Study Session From Both Profiles")
        print("14. Exit")

        choice = input("Select option: ").strip()

        if choice == "1": create_profile()
        elif choice == "2": view_profile()
        elif choice == "3": list_profiles()
        elif choice == "4": change_major()
        elif choice == "5": add_event()
        elif choice == "6": remove_event()
        elif choice == "7": sort_events()
        elif choice == "8": view_events()
        elif choice == "9": invite_two_profiles()
        elif choice == "10": accept_invite()
        elif choice == "11": decline_invite()
        elif choice == "12": auto_cancel_session()
        elif choice == "13": remove_session_from_both()
        elif choice == "14":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


  







if __name__ == "__main__":
    main()
    generate_study_sessions()