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
    



if __name__ == "__main__":
    main()