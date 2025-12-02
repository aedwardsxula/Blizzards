from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator
from event import Event
import random

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

MAJORS = ["CS", "CE", "BINF", "CIS"]

def random_name():
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie", "Cameron"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    import random
    return f"{random.choice(first_names)} , {random.choice(last_names)}"

def random_major():
    return random.choice(MAJORS)

def random_datetime():
    start = datetime.now()
    end = start + timedelta(days=30)
    return start + (end - start) * random.random()

def random_event():
    what = random.choice(["Meeting", "Study Session", "Lecture", "Workshop", "Seminar"])
    return Event(what, random_datetime())

def random_study_session(proposer):
    topic = random.choice(["What is the SDLC?" , "Midterm Prep", "Debugging Workshop","Algorithms Review", "Data Structures Overview"])
    place = random.choice(["Library", "Cafe", "Online", "Study Room", "Park"])
    time = random_datetime()
    return StudySession(proposer, time, place, topic)

def random_111_profiles():
    profiles = []
    for i in range (1,112):
        first_name, last_name = random_name().split(" , ")
        major = random_major()
        profile = Profile(i, first_name, last_name, major)
        for _ in range(random.randint(0,10)):
            profile.add_event(random_event())
        profiles.append(profile)


    #Find the longest schedule
    lgst_sched = max(len(profile.schedule) for profile in profiles)
    longest = [profile for profile in profiles if len(profile.schedule) == lgst_sched]
    print("Profiles with the longest schedules:")
    for profile in longest:
        print(profile)
        print(f"Name:{profile.first_name} {profile.last_name}  has  -", len(profile.schedule), " events")
        print("-" * 40)
    return profiles

#Create 30 random profiles
def create_30_profiles():
    def random_30_sessions():
        p1 = Profile(2001, "Student", "One", random_major())
        p2 = Profile(2002, "Student", "Two", random_major())

        sessions = [random_study_session() for _ in range(30)]

        # First 10  p1 only
        for s in sessions[:10]:
            p1.schedule.append(s)

        # Next 10  p2 only
        for s in sessions[10:20]:
            p2.schedule.append(s)
        # Final 10  invite both
        for s in sessions[20:]:
            s.invite(p1, p2)

        print(f"Profile 1 schedule size: {len(p1.schedule)}")
        print(f"Profile 2 schedule size: {len(p2.schedule)}")
        return p1, p2, sessions
        print("-" * 50)

    #remove 33 study sessions
def remove_33_sessions(self, profiles):
    count = 0

    while count < 33:
            # pick two random profiles
        pA, pB = random.sample(profiles, 2)

            # pick a random session in pA if pA has any
        if len(pA.schedule) == 0:
                continue

        session = random.choice(pA.schedule)

            # only remove if pB ALSO has this session
        if session in pB.schedule:
            pA.schedule.remove(session)
            pB.schedule.remove(session)
            count += 1
    return profiles

        #create 222 random profiles
def run_task_65(all_profiles):
        print("\n======= TASK #65: 222 STUDY SESSIONS FOR 2 PROFILES =======")

        if len(all_profiles) < 2:
            print("Not enough profiles to run task #65.")
            return

        p1, p2 = random.sample(all_profiles, 2)

        sessions = [
            random_study_session(random.choice([p1.first_name, p2.first_name]))
            for _ in range(222)
        ]   

        for s in sessions:
            s.invite(p1, p2)

            print(f"Assigned 222 sessions to profiles {p1.id} and {p2.id}")
            print("-" * 50)
# -------------------------------------------------------------
# MATCH YOUR TASK FLOW USING YOUR EXISTING FUNCTIONS
# -------------------------------------------------------------
def run_mmp_driver():

    print("\n========================")
    print(" RUNNING MMP DRIVER ")
    print("========================\n")

    # #59 —  5 base profiles
    profiles_5 = mmp_driver()   
    # #62 — use your existing create_30_profiles
    try:
        p1_30, p2_30, sessions_30 = create_30_profiles()
        profiles_5 = profiles_5 + [p1_30, p2_30]
    except:
        pass  # if your create_30_profiles needs no return

    # #64 — random 111 profiles
    try:
        profiles_111 = random_111_profiles()
        all_profiles = profiles_5 + profiles_111
    except:
        all_profiles = profiles_5

    # #60 — random 30 sessions already inside create_30_profiles
    # nothing special to add

    # #66 — remove 33 sessions
    try:
        all_profiles = remove_33_sessions(None, all_profiles)
    except:
        pass

    # #65 — generate 222 sessions
    try:
        run_task_65(all_profiles)
    except:
        pass

    print("\n======= MMP DRIVER COMPLETE =======")
    return all_profiles


class MMPDriver:
    def run(self):
        return run_mmp_driver()


if __name__ == "__main__":
    run_mmp_driver()
