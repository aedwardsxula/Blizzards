from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator

def main():
    Alex = Profile("Alex", "CIS", "Math", "Unknown")
    Alex.update_schedule({"Tuesday": ["10AM", "3PM"], "Thursday": ["1PM"]})
    print("Profile created:")
    print(Alex)

    session = StudySession(proposer=Alex, time="Mon 10am", place="Library", topic="Algorithms")
    print("\nSession proposed:", session.topic, "at", session.place)

    