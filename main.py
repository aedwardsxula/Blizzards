from datetime import datetime, timedelta
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

    syllabus = [
    {"date": datetime(2025, 11, 18), "flashcards": ["Define sorting", "Explain bubble sort"]},
    {"date": datetime(2025, 11, 20), "flashcards": ["Graph basics", "DFS vs BFS"]}
]

    generator = FlashcardGenerator(syllabus)
    cards = generator.generate(datetime(2025, 11, 18), datetime(2025, 11, 22))

    print(cards)

if __name__ == "__main__":
    main()