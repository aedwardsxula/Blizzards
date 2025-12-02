from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator
from event import Event
import random

# Global variables
profiles = []
_next_profile_id = 0

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
def run_StudyBuddy_app():
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
        print("14. View Today's Events Only")
        print("15. Exit")

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
        elif choice == "14": view_events_today()
        elif choice == "15":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")
def _next_id() -> int:
    global _next_profile_id
    val = _next_profile_id
    _next_profile_id += 1
    return val


def list_profiles():
    if not profiles:
        print("No profiles have been created yet.")
        return

    print("\n---- Current Profiles ----")
    for p in profiles:
        print(
            f"ID: {p.id} | "
            f"Name: {p.first_name} {p.last_name} | "
            f"Major: {p.major} | "
            f"Events: {len(p.schedule)}"
        )
    print("--------------------------")


def choose_profile(prompt: str = "Enter profile ID: ") -> Profile | None:
    if not profiles:
        print("No profiles available. Create one first.")
        return None

    list_profiles()
    pid_str = input(prompt).strip()
    try:
        pid = int(pid_str)
    except ValueError:
        print("Invalid ID.")
        return None

    for p in profiles:
        if p.id == pid:
            return p

    print("Profile not found.")
    return None


def _parse_datetime() -> datetime | None:
    date_str = input("Date (YYYY-MM-DD): ").strip()
    time_str = input("Time (HH:MM, 24-hour): ").strip()
    try:
        return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date/time format.")
        return None


#  MENU OPTION IMPLEMENTATIONS

def create_profile():
    print("\n--- Create Profile ---")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    major = input("Major (CS, CE, CIS, BINF): ").strip()

    try:
        p = Profile(_next_id(), first, last, major)
    except ValueError as e:
        print(f"Error creating profile: {e}")
        return

    profiles.append(p)
    print(f"Profile created: ID {p.id} for {p.first_name} {p.last_name} ({p.major})")


def view_profile():
    print("\n--- View Profile ---")
    p = choose_profile()
    if not p:
        return

    print(f"\nProfile ID: {p.id}")
    print(f"Name      : {p.first_name} {p.last_name}")
    print(f"Major     : {p.major}")
    print(f"Schedule  :")
    if not p.schedule:
        print("  (no events or sessions scheduled)")
    else:
        for item in p.schedule:
            if isinstance(item, Event):
                print(f"  - {item}")
            elif isinstance(item, StudySession):
                print(f"  - Study Session: {item.topic} at {item.time} in {item.place} [{item.status}]")
            else:
                print(f"  - {item}")


def change_major():
    print("\n--- Change Major ---")
    p = choose_profile()
    if not p:
        return

    new_major = input("Enter new major (CS, CE, CIS, BINF): ").strip()
    # use change_major method
    if hasattr(p, "change_major"):
        p.change_major(new_major)
        print(f"Major updated to {p.major}")
    else:
        p.major = new_major.upper()
        print(f"Major updated to {p.major}")


def add_event():
    print("\n--- Add Event ---")
    p = choose_profile()
    if not p:
        return

    what = input("Event description: ").strip()
    when = _parse_datetime()
    if when is None:
        return

    e = Event(what, when)
   
    e.add_event(p)


def remove_event():
    print("\n--- Remove Event ---")
    p = choose_profile()
    if not p:
        return

    if not p.schedule:
        print("No events to remove for this profile.")
        return

    what = input("Enter the event description (what) to remove: ").strip()

    dummy = Event(what, datetime.now())
    removed = p.remove_event(dummy)
    if removed:
        print(f"Removed all events with description '{what}'.")
    else:
        print(f"No events found with description '{what}'.")


def sort_events():
    print("\n--- Sort Events (Newest → Oldest) ---")
    p = choose_profile()
    if not p:
        return

    if not p.schedule:
        print("No events to sort.")
        return

    p.sort_events()
    print("Events sorted in reverse chronological order.")


def view_events():
    print("\n--- View Events ---")
    p = choose_profile()
    if not p:
        return

    if not p.schedule:
        print("No events for this profile.")
        return

    now = datetime.now()
    lines = p.output_events(now)
    for line in lines:
        print("  " + line)


def view_events_today():
    print("\n--- View Today’s Events Only ---")
    p = choose_profile()
    if not p:
        return

    if not p.schedule:
        print("No events for this profile.")
        return

    today = datetime.now().date()

    today_events = []
    for item in p.schedule:
        event_time = getattr(item, "when", getattr(item, "time", None))
        if event_time and event_time.date() == today:
            today_events.append(item)

    if not today_events:
        print("No events scheduled for today.")
        return

    print("\nToday’s Events:")
    for item in today_events:
        if isinstance(item, Event):
            print(f"  - {item}")
        elif isinstance(item, StudySession):
            print(f"  - Study Session: {item.topic} at {item.time} in {item.place} [{item.status}]")



def invite_two_profiles():
    print("\n--- Create and Invite Study Session ---")
    if len(profiles) < 2:
        print("Need at least two profiles to create a study session.")
        return

    print("Choose first invitee:")
    p1 = choose_profile("Profile ID #1: ")
    if not p1:
        return

    print("Choose second invitee:")
    p2 = choose_profile("Profile ID #2: ")
    if not p2 or p2 is p1:
        print("Second profile must be different and valid.")
        return

    topic = input("Study topic: ").strip()
    place = input("Place (Library, Online, etc.): ").strip()
    when = _parse_datetime()
    if when is None:
        return

    proposer_name = p1.first_name
    session = StudySession(proposer_name, when, place, topic)
    session.invite(p1, p2)


def _choose_session_for_profile(p: Profile) -> StudySession | None:
    """Helper: let user pick a StudySession (or subclass) from profile.schedule."""
    sessions = [s for s in p.schedule if isinstance(s, StudySession)]
    if not sessions:
        print("No study sessions found for this profile.")
        return None

    print("\nAvailable sessions:")
    for idx, s in enumerate(sessions, start=1):
        print(f"{idx}. {s.topic} at {s.time} in {s.place} [{s.status}]")

    choice = input("Choose session #: ").strip()
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(sessions):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        return None

    return sessions[idx]


def accept_invite():
    print("\n--- Accept Invite ---")
    p = choose_profile()
    if not p:
        return

    sess = _choose_session_for_profile(p)
    if not sess:
        return

    # Wrap in InviteLogic can call its method
    invite = InviteLogic(sess.proposer, sess.time, sess.place, sess.topic, status=sess.status, accepted=False)
    invite.accept_invite()

    # Replace original session in schedule with InviteLogic object
    try:
        idx = p.schedule.index(sess)
        p.schedule[idx] = invite
    except ValueError:
        # just in case it's not exactly the same object reference
        p.schedule.append(invite)


def decline_invite():
    print("\n--- Decline Invite ---")
    p = choose_profile()
    if not p:
        return

    sess = _choose_session_for_profile(p)
    if not sess:
        return

    invite = InviteLogic(sess.proposer, sess.time, sess.place, sess.topic, status=sess.status, accepted=False)
    invite.decline_invite()

    # Replace or add as needed
    try:
        idx = p.schedule.index(sess)
        p.schedule[idx] = invite
    except ValueError:
        p.schedule.append(invite)


def auto_cancel_session():
    print("\n--- Auto-Cancel Session ---")
    p = choose_profile()
    if not p:
        return

    sess = _choose_session_for_profile(p)
    if not sess:
        return

    hrs_str = input("Cancel after how many hours? (default 2): ").strip()
    try:
        hrs = int(hrs_str) if hrs_str else 2
    except ValueError:
        hrs = 2

    job = AutoCancelJob(sess.proposer, sess.time, sess.place, sess.topic, status=sess.status, cancel_after_hours=hrs)
    job.auto_cancel()

    try:
        idx = p.schedule.index(sess)
        p.schedule[idx] = job
    except ValueError:
        p.schedule.append(job)


def remove_session_from_both():
    print("\n--- Remove Study Session From Both Profiles ---")
    if len(profiles) < 2:
        print("Need at least two profiles.")
        return

    print("Choose first profile:")
    p1 = choose_profile("Profile ID #1: ")
    if not p1:
        return

    print("Choose second profile:")
    p2 = choose_profile("Profile ID #2: ")
    if not p2 or p2 is p1:
        print("Second profile must be different and valid.")
        return

    # Find sessions that both share
    common = [s for s in p1.schedule if isinstance(s, StudySession) and s in p2.schedule]
    if not common:
        print("No shared study sessions between these profiles.")
        return

    print("\nShared sessions:")
    for idx, s in enumerate(common, start=1):
        print(f"{idx}. {s.topic} at {s.time} in {s.place} [{s.status}]")

    choice = input("Choose session #: ").strip()
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(common):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        return

    sess = common[idx]
    removed = sess.remove(p1, p2)
    if removed:
        print("Study session removed from both profiles.")
    else:
        print("Nothing was removed.")

if __name__ == "__main__":
    print_welcome_banner()
    run_StudyBuddy_app()
    print("\nDriver ended")

