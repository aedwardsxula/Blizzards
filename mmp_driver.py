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
        for event in profile.schedule:
            print(f"Name:{profile.first_name} {profile.last_name}  has  -", len(profile.schedule), " events")
        print("-" * 40)
    return profiles




   

